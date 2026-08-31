# Loan Approval Logistic Regression Model

This project trains a logistic regression classifier to predict whether a loan application is approved or rejected based on applicant and loan information.

## Project Overview

The dataset includes over 45,000 loan records and contains a target variable named `loan_status`:

- `1` = approved
- `0` = rejected

The model uses a mix of numeric and categorical features, including:

- `person_gender`
- `person_education`
- `person_home_ownership`
- `loan_intent`
- `previous_loan_defaults_on_file`
- numeric financial features such as income, amount, interest rate, and credit score

The solution includes:

- data exploration and missing-value handling
- categorical encoding
- train/test split with stratification
- feature scaling with `StandardScaler`
- logistic regression training with class balancing
- evaluation metrics and visual diagnostics
- output file generation for reporting and interpretation

## How to Run

1. Open a terminal in the project folder.
2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Ensure the dataset file `loan_data.csv` is available in the project folder. If it is in another folder, you can pass the path explicitly:

```bash
python complete_ml_solution.py --data-path /path/to/loan_data.csv
```

5. Run the script:

```bash
python complete_ml_solution.py
```

## Expected Outputs

When the script runs successfully, it will produce:

- console output with model summary and metrics
- a PNG file named `logistic_regression_results.png`
- sample predictions with approval probabilities

The image includes four plots:

1. confusion matrix heatmap
2. ROC curve with AUC score
3. top 10 feature coefficients
4. prediction probability distribution

## How to Interpret Metrics

### Accuracy
Measures the percentage of total predictions that are correct.

### Precision
Of all the predicted loan approvals, how many were actually approved?

### Recall
Of all the actual approved loans, how many were correctly identified?

### F1-Score
A balanced metric between precision and recall, useful when classes are imbalanced.

### ROC-AUC
Measures how well the model distinguishes between approved and rejected loans. A value closer to 1 indicates stronger discrimination.

### Confusion Matrix
Breakdown of model decisions:

- TN: true negatives (rejected correctly)
- FP: false positives (predicted approved but actually rejected)
- FN: false negatives (predicted rejected but actually approved)
- TP: true positives (approved correctly)

## Key Findings

- Logistic regression is a strong baseline for loan approval classification because the dataset is well-structured and the target is binary.
- Class balancing helps the model handle the class imbalance that is common in approval datasets.
- Feature coefficients show which variables most strongly influence the approval decision.
- The ROC curve and AUC score help determine how well the model separates approved and rejected applications.
- The probability distribution shows the model's confidence level across predictions, which is useful for understanding risk and approval thresholds.

## Recommended Next Steps

- Tune the decision threshold if your business prefers fewer false approvals or fewer false rejections.
- Test additional models such as random forest or XGBoost for comparison.
- Use this script as a baseline before moving to more advanced production pipelines.
