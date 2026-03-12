## Keras Version Adoption Analysis

> **Note:** This is the experiment described in **Appendix B** and it produces **Figure 2**.

This folder contains:
- the BigQuery SQL query used to collect download statistics,
- the raw CSV export,
- `plot_generator.py`, which generates the plot used in the study,
- and `plot_generator.ipynb`, a notebook version of the same code.

`plot_generator.py` and `plot_generator.ipynb` contain the same analysis logic.
The notebook also includes a saved execution output (run), which is useful for quick inspection in notebook workflows.

## Goal of `plot_generator.py`

The goal of `plot_generator.py` is to visualize Keras version adoption by plotting download counts per version.

The script:
- loads the CSV dataset,
- filters out versions with fewer than `500,000` downloads,
- sorts versions by download count,
- and plots a bar chart with per-bar labels in millions.

## Requisites

- Python 3.9+ (recommended)
- Python packages:
	- `pandas`
	- `matplotlib`
- Input data file in the same folder:
	- `bquxjob_7e772f9e_1985d03a1ba.csv`

## Instructions

1. Open a terminal in this folder (`version_adoption_keras/`).
2. Install dependencies (if not already available):
	 - `pip install pandas matplotlib`
3. Run the plot script:
	 - `python plot_generator.py`
4. The plot will be displayed in an interactive window.

## Data source

The data were obtained from Google Cloud Public Datasets using BigQuery.

## Query details (`by-keras-version.sql`)

The SQL file `by-keras-version.sql` queries:
- dataset: `bigquery-public-data.pypi.file_downloads`
- package: `keras`
- time window: from `2025-03-05` to `2025-03-26`

It groups results by `file.version` and returns:
- `version`: the Keras package version string (e.g., `3.x.y`)
- `download_count`: number of download events for that version in the selected date range

Results are sorted by `download_count` in descending order.

## CSV details (`bquxjob_7e772f9e_1985d03a1ba.csv`)

This CSV is the exported result of the BigQuery job. It is the direct input consumed by `plot_generator.py`.

Expected columns:
- `version`
- `download_count`

In practice, each CSV row represents one Keras version and the total number of downloads counted for that version in the selected period.