## Summary
The Keras `Model.load_model` function permits arbitrary code execution, even with `safe_mode=True`, through a manually constructed, malicious `.keras` archive. By altering the `config.json` file within the archive, an attacker can specify arbitrary Python modules and functions, along with their arguments, to be loaded and executed during model loading.

## Details
The vulnerability affects the Keras model format `.keras`, which is used to store and load Keras models. The vulnerability allows an attacker to create a malicious `.keras` model that, when loaded, executes arbitrary code on the victim's machine. In the simplest case, a victim can be compromised simply by executing `keras.saving.load_model("model.keras")` with a malicious model. The attack works regardless of the parameter passed to `load_model`.

In particular, `keras.saving.load_model` includes a parameter `safe_mode`, which is set to `True` by default. The official Keras documentation describes `safe_mode` as:

```
safe_mode: Boolean, whether to disallow unsafe lambda deserialization. When safe_mode=False, loading an object has the potential to trigger arbitrary code execution. This argument is only applicable to the Keras v3 model format. Defaults to True.
```


Additionally, as stated in the [Keras serialization and saving documentation](https://keras.io/guides/serialization_and_saving/):

```
The saved .keras file is lightweight and does not store the Python code for custom objects. Therefore, to reload the model, `load_model` requires access to the definition of any custom objects used through one of the following methods:

1. Registering custom objects (preferred),
2. Passing custom objects directly when loading, or
3. Using a custom object scope
```


Unlike other attacks, the exploit reported here does not depend on `Lambda` layers in any way. Furthermore, it does not rely on any custom object definitions, meaning it requires no custom definitions from the victim or any additional assumptions. An attacker can create a custom model that, when parsed by Keras internals, leads to arbitrary code execution at **parsing time** (i.e., there is no need to call the model, just to load it). This is due to incorrect validation of allowed modules and some missing checks in parts of the loading code.


## Exploit
The `.keras` model format is essentially a ZIP archive containing three files: `config.json`, `metadata.json`, and `model.weights.h5`.

The [Keras documentation](https://keras.io/guides/serialization_and_saving/) describes these files as follows:

```
- A JSON-based configuration file (config.json): Records the configuration of the model, layers, and other trackables.
- A H5-based state file, such as model.weights.h5 (for the whole model), with directory keys for layers and their weights.
- A metadata file in JSON, storing information such as the current Keras version.
```

The exploit requires manually crafting a custom `config.json` and understanding some implementation details of the Keras library. This can be achieved by (quickly) reverse-engineering the Keras source code.

The exploit proposed below targets Keras versions 3.7 and 3.8. Note that this shows just one possible setup—other equivalent solutions with different execution flows may yield similar results. Additionally, different Keras versions may use slightly different naming conventions or follow different internal branches, which could require adjusting the exploit accordingly.

Most of the exploit can be summarized in the following part of the `config.json`:

```json
{
    "module": "subprocess",
    "class_name": "run",
    ...
    "inbound_nodes": [
        {
            "args": [
                "/bin/sh"
            ],
            "kwargs": {}
        }
    ]
}
```

### Bypassing Safe Loading
If we look at the Keras source code, we see that `load_model` internally calls the `deserialize_keras_object` function, located at `keras/lib/python3.12/site-packages/keras/src/saving/serialization_lib.py`. By following its execution flow, we can observe how it parses the `config.json` structure and branches based on fields like `module`, `class_name`, and other JSON elements. Indeed, Keras is designed to only allow deserialization of objects registered with the `@keras.saving.register_keras_serializable()` decorator. There are also special behaviors for certain class names, such as `__tensor__` and `__numpy__`. The `__lambda__` class is treated differently—it is only allowed when `safe_mode=False`, as it poses evident security risks.

The most interesting part comes later. If none of the previous cases match the values in `config.json`, then the following code is executed:

```python
module = config.get("module", None)
registered_name = config.get("registered_name", class_name)
...
cls = _retrieve_class_or_fn(
    class_name,
    registered_name,
    module,
    obj_type="class",
    full_config=config,
    custom_objects=custom_objects,
)
```

`_retrieve_class_or_fn` is implemented as follows:

```python
def _retrieve_class_or_fn(
    name, registered_name, module, obj_type, full_config, custom_objects=None
):
    ...
    if module:
        if module == "keras" or module.startswith("keras."):
            ...

        if obj_type == "function" and module == "builtins":
            ...

        # Otherwise, attempt to retrieve the class object given the `module`
        # and `class_name`. Import the module, find the class.
        try:
            mod = importlib.import_module(module)
        except ModuleNotFoundError:
            ...

        obj = vars(mod).get(name, None)

        ...

        if obj is not None:
            return obj

    ...
```

I've only included the most relevant code branches for clarity. As you can see, the code uses `importlib` to import the specified module and then uses `.get` to access the class specified by `class_name`. The way it extracts the class imposes some constraints on what we can import and use, but what we can do is sufficient for an exploit.

Returning to `deserialize_keras_object`, after the above code, it expects the retrieved class to be somewhat expected. In particular:

```python
if isinstance(cls, types.FunctionType):
    return cls
if not hasattr(cls, "from_config"):
    raise TypeError(
        "Unable to reconstruct an instance of '" + class_name + "' because "
        "the class is missing a `from_config()` method. "
        "Full object config: " + config
    )
```

If the class does not have the method `from_config`, Keras will raise an exception. However, if the class is a `FunctionType`, it simply returns it. `FunctionType` is different from `BuiltinsFunctionType`, making it a bit harder to find the correct function to use. However, `subprocess.run` is perfect for this purpose, fitting the entire code flow.

### Passing arbitrary arguments

Now the problem arises when we need to pass the correct arguments. In Keras, a model is seen as a graph where the output of one node is the input of the following node. We can abuse this mechanism. In the `config.json`, it is defined how a node should take inputs from other nodes, using `inbound_nodes`. Let us reverse-engineer how the code is implemented.

We focus on the `deserialize_node` function in `keras/src/models/functional.py`:

```python
def deserialize_node(node_data, created_layers):
    if not node_data:
        return [], {}

    if isinstance(node_data, list):
        ...
        return [unpack_singleton(input_tensors)], kwargs

    args = serialization_lib.deserialize_keras_object(node_data["args"])
    kwargs = serialization_lib.deserialize_keras_object(node_data["kwargs"])

    def convert_revived_tensor(x):
        ...
        return x

    args = tree.map_structure(convert_revived_tensor, args)
    kwargs = tree.map_structure(convert_revived_tensor, kwargs)
    return args, kwargs
```

Here, `node_data` is the content of `inbound_nodes`. We can see how, by passing `args` and `kwargs` as `inbound_nodes`, they are simply parsed using the same `deserialize_keras_object` seen before. If we use basic types like strings, it simply returns values without making too many checks.

When `deserialize_node` returns, the layer is called with the specified arguments:

```python
args, kwargs = deserialize_node(node_data, created_layers)
# Call layer on its inputs, thus creating the node
# and building the layer if needed.
layer(*args, **kwargs)
```
At this point, an attacker can pass `"/bin/sh"` as an example payload,  thereby obtaining the execution of `subprocess.run("/bin/sh")` and gaining a shell. Obviously, the attacker can adapt the arguments to their purposes and execute different commands.

### Proof of Concept (PoC)
The complete PoC is available.

Note that, in the provided folder, the other files of the `.keras` format (`metadata.json` and `model.weights.h5`) are not relevant and never used. They are simply taken from another non-malicious `.keras` model I created to have a complete `.keras` file.

## Attack scenario

The attacker is someone who can create a `.keras` model that is then loaded by the victim. They might, for example, upload a model on platforms like Hugging Face or similar services. The victim is only required to load the malicious model, even with `safe_mode=True` or any other parameter. No further operations are needed, and there is no need to call the model,  making it more complex for the victim to be aware of the threat. **The attack occurs during the parsing of the model.**

The attacker gains untrusted and arbitrary code execution on the victim's machine with the same permissions as the Keras application. The PoC demonstrates how it is possible to spawn a shell by calling `/bin/sh`, but any other command can also be executed.