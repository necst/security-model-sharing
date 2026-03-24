## Proof-of-Concept for SV2 (CVE-2025-54412)

Read the complete report in [`report.md`](./report.md).

Check for updates on https://github.com/io-no/CVE-Reports/issues/3

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| **Status**       | Fixed                                                           |
| **Reporter(s)**  | Gabriele Digregorio                                             |
| **CVE Record**   | [CVE-2025-54412](https://www.cve.org/CVERecord?id=CVE-2025-54412) |
| **Advisory**     | [Vendor Advisory](https://github.com/skops-dev/skops/security/advisories/GHSA-m7f4-hrc6-fwg3) |


### Instructions for Reproducibility

Run the `run.sh` script inside the `docker` folder to start a container with the correct dependencies and library versions.
The script will automatically build the Docker image, start the container, and attach you to a bash shell inside it.

Once inside the container, run the Python PoC script (`poc_load.py`). The PoC spawns a shell during model loading (after the "Press enter to load the model..." prompt).

### Expected output
```
root@3fb4835dfbe0:/poc# python poc_load.py 
Unknown types ['sklearn.linear_model._stochastic_gradient.SGDRegressor.call', 'skops.io.loads']
Press enter to load the model...
#
```