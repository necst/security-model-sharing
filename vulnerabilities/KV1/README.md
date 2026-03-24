## Proof-of-Concept for KV1 (CVE-2025-1550)

Read the complete report in [`report.md`](./report.md).

Check for updates on https://github.com/io-no/CVE-Reports/issues/2

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| **Status**       | Fixed                                                           |
| **Reporter(s)**  | Gabriele Digregorio                                             |
| **CVE Record**   | [CVE-2025-1550](https://www.cve.org/CVERecord?id=CVE-2025-1550) |
| **Advisory**     | [Vendor Advisory](https://github.com/keras-team/keras/security/advisories/GHSA-48g7-3x6r-xfhp) |


### Instructions for Reproducibility

Run the `run.sh` script inside the `docker` folder to start a container with the correct dependencies and library versions.
The script will automatically build the Docker image, start the container, and attach you to a bash shell inside it.

Once inside the container, run the Python PoC script (`poc_load.py`). The PoC spawns a shell during model loading.

### Expected output
```
root@684ca35e0cb2:/poc# python poc_load.py 
2026-03-24 19:49:07.257651: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2026-03-24 19:49:07.258113: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.
2026-03-24 19:49:07.260675: I external/local_xla/xla/tsl/cuda/cudart_stub.cc:32] Could not find cuda drivers on your machine, GPU will not be used.
2026-03-24 19:49:07.269050: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:467] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1774381747.281472      30 cuda_dnn.cc:8579] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1774381747.285321      30 cuda_blas.cc:1407] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
W0000 00:00:1774381747.296336      30 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
W0000 00:00:1774381747.296362      30 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
W0000 00:00:1774381747.296364      30 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
W0000 00:00:1774381747.296365      30 computation_placer.cc:177] computation placer already registered. Please check linkage and avoid linking the same target more than once.
2026-03-24 19:49:07.299197: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX512F AVX512_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
# 
```