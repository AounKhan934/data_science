# Data Science Course Lab - Titanic Exploratory Data Analysis (EDA)

This workspace contains the complete solutions for **Task 1: Exploratory Data Analysis on the Titanic Dataset** based on `task1.pdf`.

Each individual task from the assignment has its own dedicated, self-contained folder with its executable code (`task.py`), dataset copy, generated plots, and a documented `README.md` containing the analysis, outputs, observations, and answers to student questions.

---

## 📂 Repository Directory Structure

| Folder | Task Description | Key Output / Visualization |
| :--- | :--- | :--- |
| **[`Task_01_Import_Libraries`](./Task_01_Import_Libraries/)** | Import required libraries (numpy, pandas, matplotlib, seaborn) | Library versions & verification |
| **[`Task_02_Load_Dataset`](./Task_02_Load_Dataset/)** | Load the CSV dataset into Pandas DataFrame | Dimensions: (891, 12) |
| **[`Task_03_Display_First_Few_Rows`](./Task_03_Display_First_Few_Rows/)** | Display first 5 and 10 rows (`df.head()`) | Target, numeric & categorical features |
| **[`Task_04_Display_Random_Records`](./Task_04_Display_Random_Records/)** | Display random records (`df.sample(10)`) | Missing values observation |
| **[`Task_05_Display_General_Info`](./Task_05_Display_General_Info/)** | General technical dataset summary (`df.info()`) | Non-null counts & memory usage |
| **[`Task_06_Find_Shape`](./Task_06_Find_Shape/)** | Find rows and columns (`df.shape`) | 891 rows, 12 columns |
| **[`Task_07_Check_Data_Types`](./Task_07_Check_Data_Types/)** | Check column data types (`df.dtypes`) | 5 int64, 2 float64, 5 object |
| **[`Task_08_Count_Non_Missing_Values`](./Task_08_Count_Non_Missing_Values/)** | Count available entries (`df.notnull().sum()`) | Feature completeness metrics |
| **[`Task_09_Check_Duplicate_Rows`](./Task_09_Check_Duplicate_Rows/)** | Check duplicate records (`df.duplicated().sum()`) | 0 duplicate rows |
| **[`Task_10_Check_Target_Variable`](./Task_10_Check_Target_Variable/)** | Distinct target values (`df['Survived'].unique()`) | 0 (perished) and 1 (survived) |
| **[`Task_11_Count_Unique_Values`](./Task_11_Count_Unique_Values/)** | Count unique values per feature (`df.nunique()`) | Cardinality & identifier recognition |
| **[`Task_12_Descriptive_Statistics`](./Task_12_Descriptive_Statistics/)** | Generate descriptive statistics (`df.describe()`) | Mean/median age & fare distributions |
| **[`Task_13_Count_Missing_Values`](./Task_13_Count_Missing_Values/)** | Count missing values (`df.isnull().sum()`) | Age (177), Cabin (687), Embarked (2) |
| **[`Task_14_Columns_With_Missing_Values`](./Task_14_Columns_With_Missing_Values/)** | Filter & sort missing columns descending | Cabin (687) is highest |
| **[`Task_15_Missing_Value_Percentage`](./Task_15_Missing_Value_Percentage/)** | Calculate missing percentages | Cabin: 77.10%, Age: 19.87%, Embarked: 0.22% |
| **[`Task_16_Remove_Duplicate_Rows`](./Task_16_Remove_Duplicate_Rows/)** | Remove duplicate rows (`df.drop_duplicates()`) | 891 distinct records preserved |
| **[`Task_17_Handle_Missing_Age`](./Task_17_Handle_Missing_Age/)** | Impute missing Age with median (28.0) | Zero missing ages, outlier-resistant |
| **[`Task_18_Handle_Missing_Embarked`](./Task_18_Handle_Missing_Embarked/)** | Impute missing Embarked with mode ('S') | Zero missing embarkation ports |
| **[`Task_19_Verify_Missing_Values`](./Task_19_Verify_Missing_Values/)** | Verify dataset cleanliness after imputation | Cleaned Age & Embarked; Cabin retained |
| **[`Task_20_Overall_Survival_Rate`](./Task_20_Overall_Survival_Rate/)** | Calculate baseline passenger survival rate | Overall survival rate = **38.38%** |
| **[`Task_21_Survival_Rate_By_Sex`](./Task_21_Survival_Rate_By_Sex/)** | Compare survival rate by gender | Females: **74.20%**, Males: **18.89%** |
| **[`Task_22_Survival_Rate_By_Class`](./Task_22_Survival_Rate_By_Class/)** | Compare survival rate by ticket class | 1st: **62.96%**, 2nd: **47.28%**, 3rd: **24.24%** |
| **[`Task_23_Histograms_Numerical`](./Task_23_Histograms_Numerical/)** | Histograms for numerical variables | `histograms_numerical.png` |
| **[`Task_24_Boxplots_Outliers`](./Task_24_Boxplots_Outliers/)** | Boxplots for outlier detection | `boxplots_numerical.png` |
| **[`Task_25_Correlation_Matrix`](./Task_25_Correlation_Matrix/)** | Pairwise correlation matrix | Numeric correlation values |
| **[`Task_26_Correlation_Heatmap`](./Task_26_Correlation_Heatmap/)** | Heatmap of feature correlations | `correlation_heatmap.png` |
| **[`Task_27_Survival_Bar_Plot`](./Task_27_Survival_Bar_Plot/)** | Bar plot comparing survival by sex | `survival_by_sex.png` |
| **[`Task_28_Five_Highest_Paying_Passengers`](./Task_28_Five_Highest_Paying_Passengers/)** | Identify the 5 highest-paying passengers | Top 3 paid $512.33, 1st Class |
| **[`Task_29_Visualize_Highest_Paying`](./Task_29_Visualize_Highest_Paying/)** | Bar chart of top 5 highest-paying passengers | `top5_highest_paying.png` |

---

## 📦 Consolidated Folder

For unified analysis and reporting:
- **[`task1/`](./task1/)**:
  - `task1_eda.py`: End-to-end Python script running all 29 tasks.
  - `task1_eda.ipynb`: Interactive Jupyter Notebook.
  - `task1_report.md`: Formal lab report following Part R.
  - `plots/`: High-resolution copies of all 5 generated plots.
