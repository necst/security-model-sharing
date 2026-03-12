## Proof-of-Concept for CVE-2025-54413

Read the complete report in [`report.md`](./report.md).

Check for updates on https://github.com/io-no/CVE-Reports/issues/4

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| **Status**       | Fixed                                                           |
| **Reporter(s)**  | Gabriele Digregorio                                             |
| **CVE Record**   | [CVE-2025-54413](https://www.cve.org/CVERecord?id=CVE-2025-54413) |
| **Advisory**     | [Vendor Advisory](https://github.com/skops-dev/skops/security/advisories/GHSA-4v6w-xpmh-gfgp) |


### Instructions for Reproducibility

Run the `run.sh` script inside the `docker` folder to start a container with the correct dependencies and library versions.
The script will automatically build the Docker image, start the container, and attach you to a bash shell inside it.

Once inside the container, run the Python PoC script (`poc_load.py`). The PoC spawns a shell during model loading.