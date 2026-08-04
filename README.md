# ML Practical Notebooks

This repository contains Jupyter notebooks for machine learning practicals and small data science exercises.

## Requirements

- Python 3.10 or later
- Jupyter Notebook or JupyterLab
- `pandas`, `numpy`, `scikit-learn`, and `matplotlib`

## Step-by-Step Setup

1. Clone the repository:

```bash
git clone <your-github-repo-url>
cd "ML Praticals"
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

4. Install the required packages:

```bash
pip install pandas numpy scikit-learn matplotlib notebook
```

If you prefer JupyterLab, install it too:

```bash
pip install jupyterlab
```

5. Start Jupyter:

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

6. Open the notebook you want to run, such as `hwq1.ipynb`, and execute the cells from top to bottom.

## Included Files

- `hwq1.ipynb` - Linear regression example using temperature and ice cream sales data.
- `hwq2.ipynb` - Another practical notebook.
- `demo.ipynb`, `demo2.ipynb` - Demo notebooks.
- `data.csv`, `datahwq1.csv`, `datahwq2.csv`, `dataq2.csv` - Dataset files used by the notebooks.

## Notes

- Make sure the dataset files stay in the same folder as the notebooks.
- If a notebook does not open correctly, restart the kernel and run all cells again.
