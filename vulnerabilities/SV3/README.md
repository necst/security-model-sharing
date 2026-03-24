## Proof-of-Concept for SV3 (CVE-2025-54886)

Read the complete report in [`report.md`](./report.md).

Check for updates on https://github.com/io-no/CVE-Reports/issues/6

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| **Status**       | Fixed                                                           |
| **Reporter(s)**  | Gabriele Digregorio                                             |
| **CVE Record**   | [CVE-2025-54886](https://www.cve.org/CVERecord?id=CVE-2025-54886) |
| **Advisory**     | [Vendor Advisory](https://github.com/skops-dev/skops/security/advisories/GHSA-378x-6p4f-8jgm) |


### Instructions for Reproducibility

Run the `run.sh` script inside the `docker` folder to start a container with the correct dependencies and library versions.
The script will automatically build the Docker image, start the container, and attach you to a bash shell inside it.

Once inside the container, run the Python PoC script (`poc.py`). The PoC spawns a shell during model loading.

### Expected output
```
root@e53f6ef4ce5e:/poc# python poc.py 
#
```