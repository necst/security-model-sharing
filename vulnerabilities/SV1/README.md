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

Once inside the container, run the Python PoC script (`poc_load.py`). The PoC spawns a shell during model loading (after the "Press enter to load the model..." prompt).

### Expected output
```
root@06e1a4ad2725:/poc# python poc_load.py 
Unknown types ['builtins.int']
Press enter to load the model...
/usr/local/lib/python3.12/site-packages/sklearn/base.py:440: InconsistentVersionWarning: Trying to unpickle estimator GridSearchCV from version 1.7.1 when using version 1.7.0. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:
https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations
  warnings.warn(
#
```