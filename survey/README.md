## Survey analysis artifacts

> **Context in paper:** this experiment corresponds to **UP2 of Section 5**.

This folder contains information and analysis artifacts for the practitioner survey.

## Contents

- Survey form copy: `Survey - Model Sharing - Google Forms.pdf`
- Raw responses CSV: `Survey - Model Sharing (Responses) - Form Responses.csv`
- Statistics extraction script: `survey_script.py`
- Plot generation script: `plot_survey.py`
- Notebook equivalents of the Python scripts:
	- `survey_script.ipynb`
	- `plot_survey.ipynb`
- Wilcoxon test notebook: `wilcoxon_perception_test.ipynb`
- Generated plot artifact: `boxplot_updated.pdf`
- Docker environment: `docker/` (Dockerfile, docker-compose.yml, run.sh)

`survey_script.py` and `survey_script.ipynb` use the same analysis logic.
`plot_survey.py` and `plot_survey.ipynb` use the same plotting logic.
The notebooks already include a saved run/output for easy checking.

## Goals

- `survey_script.py` / `survey_script.ipynb`: compute descriptive statistics from responses (overall and subgroup-based).
- `plot_survey.py` / `plot_survey.ipynb`: generate the comfort-level boxplot across sharing scenarios.
- `wilcoxon_perception_test.ipynb`: run the Wilcoxon-based perception-shift validation.

## Requisites

- Python 3.9+ (recommended)
- Packages:
	- `pandas`
	- `matplotlib`
	- `scipy` (for the Wilcoxon notebook)
- Input data file in this folder:
	- `Survey - Model Sharing (Responses) - Form Responses.csv`

## Instructions

1. Open a terminal in `survey/`.
2. Install dependencies (if needed):
	 - `pip install pandas matplotlib scipy`

### Run Python scripts

- Extract statistics:
	- `python survey_script.py`
- Generate boxplot PDF:
	- `python plot_survey.py`

### Run with Docker

1. Open a terminal in `survey/docker/`.
2. Run `./run.sh` to build the Docker image and execute both `plot_survey.py` and `survey_script.py` inside the container.

### Run notebooks

- Open and run `survey_script.ipynb` for the same statistics extraction flow in notebook form.
- Open and run `plot_survey.ipynb` for the same plotting flow in notebook form.
- Open and run `wilcoxon_perception_test.ipynb` for the Wilcoxon test analysis.

### Expected outputs
- `survey_script.py`: printed statistics in the console/notebook output.
```
People who have loaded a model: 53, which is 85.48% of the total responses

People from cybersecurity count: 9, that is 16.98% of the total rows
People NOT from cybersecurity count: 44, that is 83.02% of the total rows
People from Machine Learning / Artificial Intelligence count: 33, that is 62.26% of the total rows

Average experience in ML (total): 3.4716981132075473 / 5
	Average experience in ML (cybersecurity): 3.3333333333333335 / 5
	Average experience in ML (non-cybersecurity): 3.5 / 5
	Average experience in ML (ML/AI): 3.8484848484848486 / 5

Average confidence for 'safe_mode_False': 4.509433962264151
	Cybersecurity average confidence for 'safe_mode_False': 4.888888888888889
	Non-Cybersecurity average confidence for 'safe_mode_False': 4.431818181818182
	Machine Learning / Artificial Intelligence average confidence for 'safe_mode_False': 4.515151515151516

Number of people answered with 'Arbitrary code execution' with 'safe_mode=False': 44, that is 83.02% of the total rows
	Cybersecurity people answered with 'Arbitrary code execution': 8, that is 88.89% of the cybersecurity rows
	Non-Cybersecurity people answered with 'Arbitrary code execution': 36, that is 81.82% of the non-cybersecurity rows
	Machine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': 28, that is 84.85% of the machine learning rows

Average confidence for 'safe_mode_True': 7.849056603773585
	Cybersecurity average confidence for 'safe_mode_True': 7.333333333333333
	Non-Cybersecurity average confidence for 'safe_mode_True': 7.954545454545454
	Machine Learning / Artificial Intelligence average confidence for 'safe_mode_True': 7.818181818181818

Number of people answered with 'Arbitrary code execution' with 'safe_mode=True': 8, that is 15.09% of the total rows
	Cybersecurity people answered with 'Arbitrary code execution': 4, that is 44.44% of the cybersecurity rows
	Non-Cybersecurity people answered with 'Arbitrary code execution': 4, that is 9.09% of the non-cybersecurity rows
	Machine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': 4, that is 12.12% of the machine learning rows

Average confidence for 'weights_only_False': 5.9245283018867925
	Cybersecurity average confidence for 'weights_only_False': 6.222222222222222
	Non-Cybersecurity average confidence for 'weights_only_False': 5.863636363636363
	Machine Learning / Artificial Intelligence average confidence for 'weights_only_False': 5.818181818181818

Number of people answered with 'Arbitrary code execution' with 'weights_only=False': 28, that is 52.83% of the total rows
	Cybersecurity people answered with 'Arbitrary code execution': 5, that is 55.56% of the cybersecurity rows
	Non-Cybersecurity people answered with 'Arbitrary code execution': 23, that is 52.27% of the non-cybersecurity rows
	Machine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': 17, that is 51.52% of the machine learning rows

Average confidence for 'weights_only_True': 7.037735849056604
	Cybersecurity average confidence for 'weights_only_True': 7.0
	Non-Cybersecurity average confidence for 'weights_only_True': 7.045454545454546
	Machine Learning / Artificial Intelligence average confidence for 'weights_only_True': 7.393939393939394

Number of people answered with 'Arbitrary code execution' with 'weights_only=True': 13, that is 24.53% of the total rows
	Cybersecurity people answered with 'Arbitrary code execution': 4, that is 44.44% of the cybersecurity rows
	Non-Cybersecurity people answered with 'Arbitrary code execution': 9, that is 20.45% of the non-cybersecurity rows
	Machine Learning / Artificial Intelligence people answered with 'Arbitrary code execution': 4, that is 12.12% of the machine learning rows

Number of people who inspected a model: 17, that is 32.08% of the total rows
	Number of people who inspected a model in Cybersecurity: 4, that is 44.44% of the cybersecurity rows
	Number of people who inspected a model in Non-Cybersecurity: 13, that is 29.55% of the non-cybersecurity rows
	Number of people who inspected a model in Machine Learning / Artificial Intelligence: 10, that is 30.30% of the machine learning rows

Number of people who feel MORE comfortable using HF: 39, that is 73.58% of the total rows
	Number of people who feel MORE comfortable using HF in Cybersecurity: 5, that is 55.56% of the cybersecurity rows
	Number of people who feel MORE comfortable using HF in Non-Cybersecurity: 34, that is 77.27% of the non-cybersecurity rows
	Number of people who feel MORE comfortable using HF in Machine Learning / Artificial Intelligence: 24, that is 72.73% of the machine learning rows
Number of people who feel LESS comfortable using HF: 1, that is 1.89% of the total rows
	Number of people who feel LESS comfortable using HF in Cybersecurity: 1, that is 11.11% of the cybersecurity rows
	Number of people who feel LESS comfortable using HF in Non-Cybersecurity: 0, that is 0.00% of the non-cybersecurity rows
	Number of people who feel LESS comfortable using HF in Machine Learning / Artificial Intelligence: 0, that is 0.00% of the machine learning rows
Number of people who feel EQUALLY comfortable using HF: 0, that is 0.00% of the total rows
	Number of people who feel EQUALLY comfortable using HF in Cybersecurity: 0, that is 0.00% of the cybersecurity rows
	Number of people who feel EQUALLY comfortable using HF in Non-Cybersecurity: 0, that is 0.00% of the non-cybersecurity rows
	Number of people who feel EQUALLY comfortable using HF in Machine Learning / Artificial Intelligence: 0, that is 0.00% of the machine learning rows

Number of people who answered arbitrary code execution with HF: 12, that is 22.64% of the total rows

Number of people who answered arbitrary code execution with HF in Cybersecurity: 3, that is 33.33% of the cybersecurity rows

Number of people who answered arbitrary code execution with HF in Non-Cybersecurity: 9, that is 20.45% of the non-cybersecurity rows

Number of people who answered arbitrary code execution with HF in Machine Learning / Artificial Intelligence: 7, that is 21.21% of the machine learning rows
```