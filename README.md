# Artifact Evaluation Package

This repository contains the full artifact package for the paper:

**“On the (In)Security of Loading Machine Learning Models”** *(former title: “When Secure Isn’t: Assessing the Security of Machine Learning Model Sharing”)* (IEEE S&P 2026).

The package is organized to support artifact evaluation along three dimensions:

- **Availability**: raw data, scripts, notebooks, PoCs, and model artifacts are included.
- **Reproducibility**: results can be recomputed from the provided artifacts (survey statistics/tests, plots, and PoC executions).
- **Functionality**: scripts and PoCs run as intended and produce the expected outputs.

## Mapping between folders and paper sections/results

### 1) Vulnerability PoCs

- Folder: `vulnerabilities/`
- Paper mapping:
  - `KV1`, `KV2`, `KV3` → **Section 4.1**
  - `SV1`, `SV2`, `SV3` → **Section 4.2**
- Goal: PoCs achieve arbitrary code execution at model load time, despite framework-level security measures (e.g., Keras `safe_mode`), with success indicated by spawning `/bin/sh` during loading.

Each vulnerability subfolder includes:
- a `README.md` with instructions,
- a `report.md` snapshot,
- a `docker/` environment,
- and the PoC artifacts/scripts.

To run and verify all six PoCs automatically:

```bash
cd vulnerabilities/
python3 run.py
```

### 2) Hugging Face scanning experiments

- Folder: `HF_experiments/`
- Paper mapping:
  - **Section 4.3**, **Table 3**
- Goal: availability of all PoC artifacts used for the Hugging Face tests.

### 3) Survey analysis

- Folder: `survey/`
- Paper mapping:
  - **Section 5 (UP2)**
- Goal: the provided raw responses and analysis artifacts reproduce the reported survey statistics, plots, and Wilcoxon perception-shift results.
- Contains:
  - raw survey CSV,
  - survey form copy,
  - analysis/plot scripts,
  - notebook versions,
  - Wilcoxon perception-shift test notebook,
  - `docker/` environment for reproducible execution.

### 4) Keras version adoption study

- Folder: `version_adoption_keras/`
- Paper mapping:
  - **Appendix B**, **Figure 2**
- Goal: the provided query output and plotting artifacts regenerate the same Keras version-adoption trend shown in Figure 2.
- Contains:
  - BigQuery SQL query,
  - raw CSV export,
  - script and notebook to regenerate the plot,
  - `docker/` environment for reproducible execution.

## Reports and updates

- Each vulnerability folder includes a report snapshot from paper review time.
- Updates are tracked at:
  [https://github.com/io-no/CVE-Reports](https://github.com/io-no/CVE-Reports)

## Contacts

For questions, clarifications, or collaboration inquiries:

- Gabriele Digregorio — [gabriele.digregorio@polimi.it](mailto:gabriele.digregorio@polimi.it)
- Marco Di Gennaro — [marco.digennaro@polimi.it](mailto:marco.digennaro@polimi.it)
- Stefano Zanero — [stefano.zanero@polimi.it](mailto:stefano.zanero@polimi.it)
- Stefano Longari — [stefano.longari@polimi.it](mailto:stefano.longari@polimi.it)
- Michele Carminati — [michele.carminati@polimi.it](mailto:michele.carminati@polimi.it)
