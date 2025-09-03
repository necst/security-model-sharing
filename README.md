# Security Model Sharing – Artifacts and Proof-of-Concepts
This repository hosts the complete set of artifacts supporting the paper:

“Secure by Name, Vulnerable by Design: On the (In)Security of Machine Learning Model Sharing.”

All materials are released in the spirit of open science, enabling others to evaluate and reproduce our findings.

## Repository Contents

* **CVE Proof-of-Concepts (PoCs)**

  * Each folder (e.g., `CVE-2025-1550/`, `CVE-2025-54412/`, etc.) contains:

    * The complete report as it was published at paper review time (`report.md`).
    * Information on the vulnerability, references, and links to check for updates (`README.md`).    
    * Reproducibility scripts, Docker containers, and complete PoCs for the corresponding CVE.

* **HF Experiments – Model Artifacts**

  * Model artifacts uploaded to Hugging Face for evaluation.
  * Associated scripts for generating these models.

* **Survey Data and Tools**

  * Raw survey responses (CSV format).
  * The questionnaire as distributed to participants.
  * Collection scripts and statistical analysis code.

* **Version Adoption (Keras)**

  * Scripts and data supporting the study in the appendix on Keras version adoption.

## Usage

**Disclaimer:** The provided code and artifacts are for research and educational purposes only.
They demonstrate security issues in machine learning model sharing and must **not** be used for malicious purposes.

To reproduce a PoC:

1. Navigate to the relevant CVE folder.
2. Read the `report.md` for context.
3. Check the provided link for the latest updates.
4. Follow the instructions in `README.md` to run the PoC in a controlled environment.

## Reports and Updates

* Each CVE folder includes a snapshot of the report at paper review time.
* Updates are tracked in:
  [https://github.com/io-no/CVE-Reports](https://github.com/io-no/CVE-Reports)


## Contact
For questions, clarifications, or collaboration inquiries, please reach out to the authors:

* Gabriele Digregorio — [gabriele.digregorio@polimi.it](mailto:gabriele.digregorio@polimi.it)
* Marco Di Gennaro — [marco.digennaro@polimi.it](mailto:marco.digennaro@polimi.it)
* Stefano Zanero — [stefano.zanero@polimi.it](mailto:stefano.zanero@polimi.it)
* Stefano Longari — [stefano.longari@polimi.it](mailto:stefano.longari@polimi.it)
* Michele Carminati — [michele.carminati@polimi.it](mailto:michele.carminati@polimi.it)
