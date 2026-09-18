# Task 1: Exploratory Data Analysis on the Titanic Dataset

This folder contains the complete solution, source code, interactive notebook, visualizations, and lab report for **Task 1: Exploratory Data Analysis on the Titanic Dataset** based on `task1.pdf`.

---

## 📁 Folder Contents

- **`Titanic-Dataset.csv`**: The dataset containing 891 passenger records across 12 features.
- **`task1_eda.py`**: Python script executing all 29 tasks step-by-step, generating statistical outputs and saving all plots.
- **`task1_eda.ipynb`**: Interactive Jupyter Notebook with documentation, code blocks, outputs, and student question answers.
- **`task1_report.md`**: Comprehensive lab report formatted strictly according to the submission requirements (Part R):
  - Task investigation description
  - Python code
  - Execution output
  - Observations under each major task
  - Answers to Student Questions and Part P (Questions 1 to 14)
  - Final Conclusion (5 to 8 lines)
- **`plots/`**: Directory containing publication-quality figures:
  - `histograms_numerical.png` (Task 23: Distributions for Age, Fare, SibSp, Parch)
  - `boxplots_numerical.png` (Task 24: Outlier detection across numerical attributes)
  - `correlation_heatmap.png` (Task 26: Annotated correlation heatmap)
  - `survival_by_sex.png` (Task 27: Average survival rate by sex)
  - `top5_highest_paying.png` (Task 29: Top 5 highest paying passengers)

---

## 🚀 How to Run

1. **Run Python Script**:
   ```bash
   python task1_eda.py
   ```

2. **Run Jupyter Notebook**:
   ```bash
   jupyter notebook task1_eda.ipynb
   ```

---

## 📊 Key Summary Findings

- **Overall Survival Rate:** 38.38% (342 survivors out of 891).
- **Gender Disparity:** 74.20% female survival vs. 18.89% male survival (~4x difference due to "women and children first").
- **Socioeconomic Stratification:** 1st Class (62.96%), 2nd Class (47.28%), 3rd Class (24.24%).
- **Data Cleaning:** Imputed missing `Age` (177 missing) with median (28.0) and `Embarked` (2 missing) with mode ('S'). `Cabin` retained as-is due to 77.10% missingness.
