## Summary
`skops` is a Python library for securely sharing scikit-learn-based models without using pickle. However, an inconsistency in `MethodNode` can be exploited to access unexpected object fields through dot notation. This can be used to achieve **arbitrary code execution at load time**.


## Details
A `skops` model is a ZIP file containing various files, including a `schema.json` that represents the model structure in a tree-like format. Each node in the tree can have different types, among those expected by `skops`. These types include `MethodNode`, `TypeNode`, `FunctionNode`, and others. The intended workflow is to inspect the model using the `skops` API's `get_untrusted_types` function, which identifies types not considered trusted by default. The user is expected to review these types and, if deemed secure, explicitly pass them to the `load` function. The `load` function will then load the model, but it will raise an error if any untrusted types remain unapproved.

This report will focus on the `MethodNode`, which allows access to attributes of existing objects via dot notation. However, there are several critical shortcomings:

* Although the `__class__` and `__module__` fields are checked via `get_untrusted_types` and during the `load` phase (as a concatenated string), **they are not actually used by `MethodNode`**. Instead, the `func` and `obj` entries in the `schema.json` are used to determine the behavior. This means that even an apparently harmless `__module__.__class__` pair can lead to access of arbitrary attributes or methods of loaded objects, without any additional checks.

* **Nothing prevents an attacker from chaining multiple `MethodNode` instances** to traverse the object hierarchy and access harmful attributes.

For example, an object can be loaded using the `ObjectNode`, which normally enforces strict checks and allows only trusted or explicitly permitted objects. However, once the object is loaded, dot notation can be used to access any of its attributes or methods. Furthermore, by chaining multiple `MethodNode`s, one can traverse the Python object hierarchy and reach dangerous components such as the `builtins` dictionary—which contains functions like `exec` and `eval`.

This vulnerability allows the attacker to **bypass both `get_untrusted_types` and `load` checks**, enabling access to dangerous attributes and methods without triggering any alerts. As demonstrated in the PoC, arbitrary code execution is possible using just an anonymous object returned by `get_untrusted_types` (in the example, `builtins.int`, though any type would suffice since it doesn't influence the exploit).


For example, consider a malicious `schema.json` snippet like:

```json
...
"__class__": "int",
"__module__": "builtins",
"__loader__": "MethodNode",
"content": {
  "obj": {
    "__class__": "int",
    "__module__": "builtins",
    "__loader__": "MethodNode",
    "content": {
      "obj": {
        "__class__": "QuadraticDiscriminantAnalysis",
        "__module__": "sklearn.discriminant_analysis",
        "__loader__": "ObjectNode",
        "__id__": 1
      },
      "func": "decision_function"
    }
  },
  "func": "__builtins__"
}
...
```

Here, the attacker loads a trusted `QuadraticDiscriminantAnalysis` object using `ObjectNode`, accesses its `decision_function` method via `MethodNode`, and then uses another `MethodNode` to access the `__builtins__` dictionary—**all without triggering the untrusted type detection mechanisms**.


## Exploit

The provided exploit demonstrates arbitrary code execution using only `builtins.int` as the type returned by `get_untrusted_types` and verified by `load`. Note that the actual type is fully controlled by the attacker and can be anything (e.g., `provola.whatever`), as it's not used by the actual `load` or the exploit logic.

### Components Used in the Exploit

To craft the exploit, I used the following `skops` nodes:

* **`MethodNode`** – to silently access arbitrary Python attributes via dot notation. This is the vulnerable core.
* **`ObjectNode`** – to load a trusted object and use it as a base to access its attributes and methods. Also used to set object state via `__setstate__`.
* **`PartialNode`** – to easily control arguments passed to functions accessed.
* **`DefaultDictNode`** – to store a crafted call to `exec` using the `default_factory` attribute.
* **`DictNode`** – to trigger the call at load time.
* **`JsonNode`, `TypeNode`, `ListNode`**, etc. – for basic types, structures, and constants.

Additionally, the interesting implementation of `GridSearchCV.score` was leveraged, specifically:

```python
def score(self, X, y=None, **params):
    ...
    scorer = self.scorer_[self.refit]
    return scorer(self.best_estimator_, X, y, **score_params)
```


### Exploit Logic (Python Equivalent)
The `schema.json` used in this exploit is quite complex and carefully constructed. For this reason, I prefer to illustrate the exploit logic using the following Python code, which presents the core idea in a simplified and readable format. It simulates how the malicious `schema.json` is interpreted and executed by `skops` during model loading. This code demonstrates how an attacker can manipulate trusted objects and attributes using `MethodNode` and chain multiple nodes, ultimately gaining access to the `__builtins__` dictionary and invoking `exec` with a controlled payload, hence achieving arbitrary code execution.


```python
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.model_selection._search import GridSearchCV
from functools import partial
from collections import defaultdict

# Step 1: Access builtins via dot traversal
a = QuadraticDiscriminantAnalysis().decision_function.__builtins__

# Step 2: Prepare GridSearchCV with overridden attributes
b = GridSearchCV()
b._sklearn_version = "1.7.0"
... # Less interesting attributes
b.scorer_ = a  # builtins dict
b.refit = "exec"
b.best_estimator_ = "import os; os.system('/bin/sh')"

# Step 3: Create callable chain
c = b.score
d = partial(c, {}, {})  # empty dicts as globals/locals
e = defaultdict(**{})
e.default_factory = d
f = e.__getitem__  # dot traversal again :)

# Step 4: Force __getitem__ with a missing key to trigger default_factory
```

What we can see here is that, when `f` is called, it invokes the `__getitem__` method of a `defaultdict`. Since the requested key doesn’t exist (the dict is empty), `default_factory` is triggered, which is the partial function `d`, wrapping the `score` method of the loaded `GridSearchCV` object.

Critically, the attributes of the `GridSearchCV` object (`scorer_`, `refit`, and `best_estimator_`) have been overwritten so that:

* `scorer_` is the `__builtins__` dictionary,
* `refit` is set to `exec`, selecting the `exec` function from `__builtins__`,
* `best_estimator_` contains the malicious payload: `"import os; os.system('/bin/sh')"`.

When `score()` is eventually called via the partial function, it resolves `self.scorer_[self.refit]` to `exec`, and then calls it as:

```python
exec(self.best_estimator_, {}, {})
```

In other words:

```python
exec("import os; os.system('/bin/sh')", {}, {})
```

This leads to **arbitrary command execution**.

Finally, to trigger this chain, it's sufficient to force a call to `f` (i.e., `__getitem__`) with a key that doesn’t exist. This can be done at model load time using `DictNode`. We use the implementation of `DictNode._construct()`:

```python
def _construct(self):
    content = gettype(self.module_name, self.class_name)()
    key_types = self.children["key_types"].construct()
    for k_type, (key, val) in zip(key_types, self.children["content"].items()):
        content[k_type(key)] = val.construct()
    return content
```

By setting `key_types = [f]` and using a missing key, the exploit executes during model loading.

### What is shown when loading the model

Suppose a user loads the model with the following code:

```python
from skops.io import load, get_untrusted_types

unknown_types = get_untrusted_types(file="model.skops")
print("Unknown types", unknown_types)
input("Press enter to load the model...")
loaded = load("model.skops", trusted=unknown_types)
```

The output will be:

```
Unkonown types ['builtins.int']
Press enter to load the model...
```

However, the model loading will trigger the execution of the payload, which in this case is a shell command. The same can be modified to execute any arbitrary code.

### Proof of Concept (PoC)
The complete malicious `skops` model is provided for reference and reproducibility. The PoC is available.

## Attack scenario

An attacker can craft a malicious model file that, when loaded, executes **arbitrary code** on the victim’s machine. This occurs **at load time**, requiring no user interaction beyond loading the model. Given that `skops` is often used in collaborative environments and is designed with security in mind, this vulnerability poses a significant threat.