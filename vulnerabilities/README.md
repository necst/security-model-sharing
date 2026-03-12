# Vulnerabilities PoCs

This folder contains proof-of-concept (PoC) exploits for Keras and skops vulnerabilities.

> **Context in paper:**
> - `KV1`, `KV2`, `KV3` correspond to the content of **Section 4.1**.
> - `SV1`, `SV2`, `SV3` correspond to the content of **Section 4.2**.

## Goal and success criteria

For every PoC in this folder, the exploit goal is to spawn `/bin/sh`.
A PoC run is considered **successful** if a shell is executed while the PoC is running.

## Folder structure

```text
vulnerabilities/
├── KV1/   # Keras vulnerability PoC (CVE-2025-1550)
├── KV2/   # Keras vulnerability PoC (CVE-2025-9906, CVE-2025-8747)
├── KV3/   # Keras vulnerability PoC (CVE-2025-9905)
├── SV1/   # skops vulnerability PoC (CVE-2025-54413)
├── SV2/   # skops vulnerability PoC (CVE-2025-54412)
└── SV3/   # skops vulnerability PoC (CVE-2025-54886)
```

Each vulnerability folder includes:
- a local `README.md` and `report.md`
- a `docker/` folder with `Dockerfile` and `run.sh`
- PoC model/script artifacts

## Prerequisites

- Docker installed and running
- Ability to run interactive containers (`docker run -it ...`)

## How to run each PoC

The execution pattern is the same for all cases:
1. Open a terminal in the PoC-specific `docker/` folder.
2. Run `./run.sh` to build and start the container shell.
3. Inside the container (`/poc`), execute the PoC loader script (e.g., `python poc_load.py`).
4. Confirm that a shell is spawned (`/bin/sh`).

---

### KV1 (CVE-2025-1550)

- Host:
  - `cd vulnerabilities/KV1/docker`
  - `./run.sh`
- In container:
  - `python poc_load.py`

### KV2 (CVE-2025-9906, CVE-2025-8747)

- Host:
  - `cd vulnerabilities/KV2/docker`
  - `./run.sh`
- In container:
  - `python poc_load.py`

### KV3 (CVE-2025-9905)

- Host:
  - `cd vulnerabilities/KV3/docker`
  - `./run.sh`
- In container:
  - `python poc_load.py`

### SV1 (CVE-2025-54413)

- Host:
  - `cd vulnerabilities/SV1/docker`
  - `./run.sh`
- In container:
  - `python poc_load.py`

### SV2 (CVE-2025-54412)

- Host:
  - `cd vulnerabilities/SV2/docker`
  - `./run.sh`
- In container:
  - `python poc_load.py`

### SV3 (CVE-2025-54886)

- Host:
  - `cd vulnerabilities/SV3/docker`
  - `./run.sh`
- In container:
  - `python poc_load.py`

## Notes

- These PoCs are for security research and controlled testing only.
- For technical details and disclosure context, see each vulnerability subfolder `report.md`.
