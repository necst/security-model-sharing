# HF Experiments Artifacts

This folder contains the exact artifacts as uploaded to Hugging Face.
These uploads are the ones that produced the scanning results reported in **Section 4.3** (see **Table 3**).

## Artifact groups

### Keras vulnerability-related artifacts

- `KV1.keras`
- `KV2_no_download.keras`
- `KV2_download.keras`

> **Important:** `KV3` and `baseline_malicious_lambda` are the same artifact in practice (same malicious Lambda-based behavior), so `KV3` is **not repeated** separately in this folder/table mapping.

### skops vulnerability-related artifacts

- `SV1.skops`
- `SV2.skops`
- `SV3.skops`

### Baseline artifacts

Located in [Baseline/](Baseline/):

- `baseline_malicious_lambda.keras`
- `baseline_malicious_lambda.h5`
- `baseline_non_malicious_lambda.keras`
- `baseline_non_malicious_lambda.h5`
- `baseline_no_lambda.keras`
- `baseline_no_lambda.h5`
- `generate_baselines.py`: generates the baseline Keras models above (malicious Lambda, non-malicious Lambda, and no-Lambda variants in both `.keras` and `.h5` formats).

### Pickle extension experiment artifacts

Located in [Pickle-Test/](Pickle-Test/):

- `save_pickle.py`
- `load_pickle.py`
- generated files with multiple extensions (`.keras`, `.h5`, `.json`, `.onnx`, `.pt`, `.skops`, `.txt`, etc.)

Script roles:

- `save_pickle.py`: creates a malicious pickle payload object and writes it to files with different extensions to test extension-based handling/scanning behavior.
- `load_pickle.py`: loads one of those files with Python `pickle` to show payload execution at deserialization time.