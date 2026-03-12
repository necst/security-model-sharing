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

### Run notebooks

- Open and run `survey_script.ipynb` for the same statistics extraction flow in notebook form.
- Open and run `plot_survey.ipynb` for the same plotting flow in notebook form.
- Open and run `wilcoxon_perception_test.ipynb` for the Wilcoxon test analysis.