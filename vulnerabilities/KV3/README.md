## Proof-of-Concept for KV3 (CVE-2025-9905)

Read the complete report in [`report.md`](./report.md).

Check for updates on https://github.com/io-no/CVE-Reports/issues/7

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| **Status**       | Fixed                                                           |
| **Reporter(s)**  | Gabriele Digregorio                                             |
| **CVE Record**   | [CVE-2025-9905](https://www.cve.org/CVERecord?id=CVE-2025-9905) |
| **Advisory**     | [Vendor Advisory](https://github.com/keras-team/keras/security/advisories/GHSA-36rr-ww3j-vrjv) |


### Instructions for Reproducibility

Run the `run.sh` script inside the `docker` folder to start a container with the correct dependencies and library versions.
The script will automatically build the Docker image, start the container, and attach you to a bash shell inside it.

Once inside the container, run the Python PoC script (`poc_load.py`). The PoC spawns a shell during model loading.