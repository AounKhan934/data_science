# Task 1: Exploratory Data Analysis on the Titanic Dataset
**Course / Lab Submission Report**

---

## 2. Objective
The objective of this lab is to learn how to perform **Exploratory Data Analysis (EDA)** on a CSV dataset using Python.

After completion, students should be able to:
- Load a CSV dataset into Python.
- Inspect rows, columns, and data types.
- Identify missing values and duplicate records.
- Study unique values in columns.
- Calculate basic statistical information.
- Clean missing and duplicate data.
- Perform simple group-based analysis.
- Create histograms, boxplots, bar plots, and heatmaps.
- Interpret patterns found during EDA.

---

## 3. Dataset Overview
The Titanic passenger dataset contains 891 records and 12 features representing passenger demographics, ticket information, and survival status:
- `PassengerId`: Unique passenger identification number.
- `Survived`: Survival indicator (`0` = Did not survive, `1` = Survived).
- `Pclass`: Ticket passenger class (`1` = 1st Class / Upper, `2` = 2nd Class / Middle, `3` = 3rd Class / Lower).
- `Name`: Full name of the passenger.
- `Sex`: Passenger biological sex (`male`, `female`).
- `Age`: Passenger age in years.
- `SibSp`: Number of siblings or spouses travelling with the passenger.
- `Parch`: Number of parents or children travelling with the passenger.
- `Ticket`: Ticket number string.
- `Fare`: Passenger fare paid.
- `Cabin`: Cabin number.
- `Embarked`: Port of embarkation (`C` = Cherbourg, `Q` = Queenstown, `S` = Southampton).

---

# Detailed Task Walkthrough (Tasks 1 – 29)

---

### Part A – Setting Up Python

#### Task 1: Import the Required Libraries
- **Task:** What are we investigating?  
  Importing the foundational numerical and data analysis libraries (`numpy`, `pandas`) and plotting libraries (`matplotlib.pyplot`, `seaborn`) required for exploratory data analysis.
- **Code:**
  ```python
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt
  import seaborn as sns
  ```
- **Output:**
  Libraries loaded into Python environment without errors.
- **Observation:**
  All four core data science libraries are available, enabling DataFrame operations and publication-grade visualizations.

---

### Part B – Loading the Dataset

#### Task 2: Load the CSV File
- **Task:** What are we investigating?  
  Reading the raw CSV data into a Pandas DataFrame so that structured tabular operations can be executed.
- **Code:**
  ```python
  df = pd.read_csv("Titanic-Dataset.csv")
  ```
- **Output:**
  DataFrame initialized with 891 rows and 12 columns.
- **Observation:**
  The dataset was parsed cleanly into memory with proper header recognition.

---

### Part C – Initial Dataset Inspection

#### Task 3: Display the First Few Rows
- **Task:** What are we investigating?  
  Examining the first 5 and 10 rows to view column names, data layout, and sample entries.
- **Code:**
  ```python
  df.head()
  df.head(10)
  ```
- **Output:**
  ```
     PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
  0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
  1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
  2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
  3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
  4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S
  ```
- **Observation:**
  - The target column is clearly identified as `Survived`.
  - Numerical columns include: `PassengerId`, `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`.
  - Categorical or text columns include: `Name`, `Sex`, `Ticket`, `Cabin`, `Embarked`.

#### Task 4: Display Random Records
- **Task:** What are we investigating?  
  Selecting 10 random records to avoid bias towards the top of the file and inspect data variation across the entire dataset.
- **Code:**
  ```python
  df.sample(10, random_state=42)
  ```
- **Output:**
  A representative cross-section of 10 rows from throughout the dataset.
- **Observation:**
  Random rows consistently show missing entries represented as `NaN`, particularly in `Cabin` and `Age`.

---

### Part D – Understanding Dataset Structure

#### Task 5: Display General Dataset Information
- **Task:** What are we investigating?  
  Checking non-null counts, column data types, total rows, and memory usage.
- **Code:**
  ```python
  df.info()
  ```
- **Output:**
  ```
  <class 'pandas.DataFrame'>
  RangeIndex: 891 entries, 0 to 890
  Data columns (total 12 columns):
   #   Column       Non-Null Count  Dtype  
  ---  ------       --------------  -----  
   0   PassengerId  891 non-null    int64  
   1   Survived     891 non-null    int64  
   2   Pclass       891 non-null    int64  
   3   Name         891 non-null    object 
   4   Sex          891 non-null    object 
   5   Age          714 non-null    float64
   6   SibSp        891 non-null    int64  
   7   Parch        891 non-null    int64  
   8   Ticket       891 non-null    object 
   9   Fare         891 non-null    float64
   10  Cabin        204 non-null    object 
   11  Embarked     889 non-null    object 
  dtypes: float64(2), int64(5), object(5)
  memory usage: 83.7+ KB
  ```
- **Observation (Student Questions):**
  1. *How many columns are present?* **12 columns**.
  2. *Which columns contain numerical data?* **PassengerId, Survived, Pclass, Age, SibSp, Parch, Fare**.
  3. *Which columns contain text or categorical data?* **Name, Sex, Ticket, Cabin, Embarked**.
  4. *Which columns appear to contain missing values?* **Age** (714 non-null), **Cabin** (204 non-null), and **Embarked** (889 non-null).

#### Task 6: Find the Number of Rows and Columns
- **Task:** What are we investigating?  
  Measuring the exact dimensional shape of the dataset.
- **Code:**
  ```python
  df.shape
  ```
- **Output:**
  `(891, 12)`
- **Observation:**
  - Number of rows = **891**
  - Number of columns = **12**

#### Task 7: Check the Data Type of Every Column
- **Task:** What are we investigating?  
  Verifying the storage data type assigned to each column.
- **Code:**
  ```python
  df.dtypes
  ```
- **Output:**
  `PassengerId` (int64), `Survived` (int64), `Pclass` (int64), `Name` (object), `Sex` (object), `Age` (float64), `SibSp` (int64), `Parch` (int64), `Ticket` (object), `Fare` (float64), `Cabin` (object), `Embarked` (object).
- **Observation:**
  There are 5 integer columns, 2 float columns, and 5 object (string/categorical) columns.

---

### Part E – Missing and Duplicate Data

#### Task 8: Count Non-Missing Values
- **Task:** What are we investigating?  
  Counting how many valid, populated entries exist in each feature.
- **Code:**
  ```python
  df.notnull().sum()
  ```
- **Output:**
  Most columns have 891 non-null entries, whereas `Age` has 714, `Cabin` has 204, and `Embarked` has 889.
- **Observation:**
  The non-missing counts confirm that data completeness is high for demographics and ticketing, but sparse for cabin numbers.

#### Task 9: Check Duplicate Rows
- **Task:** What are we investigating?  
  Determining if identical passenger records were accidentally duplicated in the dataset.
- **Code:**
  ```python
  print("Duplicate Rows:", df.duplicated().sum())
  ```
- **Output:**
  `Duplicate Rows: 0`
- **Observation:**
  There are **0 duplicate rows** in the dataset; all 891 records represent distinct passenger instances.

---

### Part F – Understanding Unique Values

#### Task 10: Check the Values of the Target Variable
- **Task:** What are we investigating?  
  Finding the discrete classes present in the primary prediction target `Survived`.
- **Code:**
  ```python
  df["Survived"].unique()
  ```
- **Output:**
  `array([0, 1], dtype=int64)`
- **Observation:**
  - `0` represents passengers who did not survive (died).
  - `1` represents passengers who survived.

#### Task 11: Count Unique Values in Every Column
- **Task:** What are we investigating?  
  Distinguishing between low-cardinality categorical variables, discrete counts, and high-cardinality identifiers.
- **Code:**
  ```python
  df.nunique()
  ```
- **Output:**
  ```
  PassengerId    891
  Survived         2
  Pclass           3
  Name           891
  Sex              2
  Age             88
  SibSp            7
  Parch            7
  Ticket         681
  Fare           248
  Cabin          147
  Embarked         3
  dtype: int64
  ```
- **Observation (Student Questions):**
  1. *Which columns contain very few unique values?* `Survived` (2), `Sex` (2), `Pclass` (3), `Embarked` (3).
  2. *Which columns appear to work as identifiers?* `PassengerId` (891 distinct values, exact unique key), `Name` (891), and `Ticket` (681).
  3. *Which columns may be categorical?* `Survived`, `Pclass`, `Sex`, `Embarked`.

---

### Part G – Statistical Summary

#### Task 12: Generate Descriptive Statistics
- **Task:** What are we investigating?  
  Computing central tendencies, spreads, and range metrics for all continuous and discrete numerical columns.
- **Code:**
  ```python
  df.describe()
  ```
- **Output:**
  ```
         PassengerId    Survived      Pclass         Age       SibSp       Parch        Fare
  count   891.000000  891.000000  891.000000  714.000000  891.000000  891.000000  891.000000
  mean    446.000000    0.383838    2.308642   29.699118    0.523008    0.381594   32.204208
  std     257.353842    0.486592    0.836071   14.526497    1.102743    0.806057   49.693429
  min       1.000000    0.000000    1.000000    0.420000    0.000000    0.000000    0.000000
  25%     223.500000    0.000000    2.000000   20.125000    0.000000    0.000000    7.910400
  50%     446.000000    0.000000    3.000000   28.000000    0.000000    0.000000   14.454200
  75%     668.500000    1.000000    3.000000   38.000000    1.000000    0.000000   31.000000
  max     891.000000    1.000000    3.000000   80.000000    8.000000    6.000000  512.329200
  ```
- **Observation (Student Questions):**
  1. Average passenger age: **29.70 years**
  2. Minimum passenger age: **0.42 years** (~5 months old)
  3. Maximum passenger age: **80.00 years**
  4. Average fare: **$32.20**
  5. Maximum fare: **$512.33**
  6. Median age: **28.00 years**
  - *Observation Summary:* The average age of passengers is approximately **29.70 years**. Passenger fares range from **$0.00 to $512.33**. The large difference between the median ($14.45) and maximum Fare ($512.33) indicates that some passengers paid much higher fares than most passengers, reflecting significant positive skewness.

---

### Part H – Detailed Missing-Value Analysis

#### Task 13: Count Missing Values
- **Task:** What are we investigating?  
  Quantifying null elements per column.
- **Code:**
  ```python
  df.isnull().sum()
  ```
- **Output:**
  `Age`: 177, `Cabin`: 687, `Embarked`: 2. All other columns: 0.

#### Task 14: Display Only Columns with Missing Values
- **Task:** What are we investigating?  
  Filtering and sorting columns with missing values in descending order.
- **Code:**
  ```python
  missing_values = df.isnull().sum()
  missing_values[missing_values > 0].sort_values(ascending=False)
  ```
- **Output:**
  `Cabin` (687), `Age` (177), `Embarked` (2).
- **Observation:**
  `Cabin` has the largest number of missing values.

#### Task 15: Calculate Missing-Value Percentage
- **Task:** What are we investigating?  
  Assessing missing data severity by relative percentage.
- **Code:**
  ```python
  missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
  pd.DataFrame({
      "Missing Count": df.isnull().sum(),
      "Missing Percentage": missing_percentage
  })
  ```
- **Output:**
  | Column | Missing Count | Missing Percentage |
  | :--- | :--- | :--- |
  | Cabin | 687 | 77.10% |
  | Age | 177 | 19.87% |
  | Embarked | 2 | 0.22% |
- **Observation (Student Questions):**
  1. *Column with highest missing percentage:* **Cabin** (77.10%).
  2. *Is missing percentage in Age small or significant?* **Significant** (~19.87%, 1 in 5 passengers). Dropping rows would lose 20% of data, requiring imputation.
  3. *Does Embarked contain many missing values?* **No**, only 2 missing entries (0.22%).
  4. *Would filling Cabin be reliable if most values are missing?* **No**, because over 77% of entries are absent. Imputing would introduce artificial noise and unfounded assumptions.

---

### Part I – Data Cleaning

#### Task 16: Remove Duplicate Rows
- **Task:** What are we investigating?  
  Eliminating redundant rows to ensure clean analysis.
- **Code:**
  ```python
  df = df.drop_duplicates().copy()
  ```
- **Output:**
  Dataset retains all 891 records (0 duplicates found).
- **Observation:**
  The dataset was confirmed free from duplicate observations.

#### Task 17: Handle Missing Age Values
- **Task:** What are we investigating?  
  Imputing missing `Age` values using the median.
- **Code:**
  ```python
  median_age = df["Age"].median() # 28.0
  df["Age"] = df["Age"].fillna(median_age)
  ```
- **Output:**
  All 177 missing age values populated with 28.0.
- **Observation:**
  Median was selected over mean because age distribution can contain extremes; median is robust against outlier distortion.

#### Task 18: Handle Missing Embarked Values
- **Task:** What are we investigating?  
  Imputing missing categorical port values using the statistical mode.
- **Code:**
  ```python
  mode_embarked = df["Embarked"].mode()[0] # 'S'
  df["Embarked"] = df["Embarked"].fillna(mode_embarked)
  ```
- **Output:**
  Both missing values filled with 'S' (Southampton).
- **Observation:**
  'S' is overwhelmingly the most frequent boarding port (>72%), making it the most probable class for the missing records.

#### Task 19: Verify Missing Values After Cleaning
- **Task:** What are we investigating?  
  Validating post-cleaning state of the DataFrame.
- **Code:**
  ```python
  df.isnull().sum()
  ```
- **Output:**
  `Age`: 0, `Embarked`: 0, `Cabin`: 687.
- **Observation (Student Questions):**
  1. *Does Age still contain missing values?* **No** (0).
  2. *Does Embarked still contain missing values?* **No** (0).
  3. *Which column still contains a large number of missing values?* **Cabin** (687), deliberately kept unmodified as per instructions.

---

### Part J – Group-Level Analysis

#### Task 20: Calculate the Overall Survival Rate
- **Task:** What are we investigating?  
  Determining the baseline passenger survival percentage.
- **Code:**
  ```python
  survival_rate = df["Survived"].mean() * 100
  print(f"Overall Survival Rate: {survival_rate:.2f}%")
  ```
- **Output:**
  `Overall Survival Rate: 38.38%`
- **Observation:**
  Overall survival rate = **38.38%** (approximately 38 out of 100 passengers survived).

#### Task 21: Compare Survival Rate by Sex
- **Task:** What are we investigating?  
  Comparing survival rates between males and females.
- **Code:**
  ```python
  df.groupby("Sex")["Survived"].mean() * 100
  ```
- **Output:**
  - Female: **74.20%**
  - Male: **18.89%**
- **Observation (Student Questions):**
  1. *Survival rate for females:* **74.20%**
  2. *Survival rate for males:* **18.89%**
  3. *Which group had higher survival rate?* **Females**
  4. *Is the difference small or large?* **Extremely large** (difference of 55.31 percentage points; females were almost 4x more likely to survive).

#### Task 22: Compare Survival Rate by Passenger Class
- **Task:** What are we investigating?  
  Investigating the relationship between socioeconomic class (`Pclass`) and survival.
- **Code:**
  ```python
  df.groupby("Pclass")["Survived"].mean() * 100
  ```
- **Output:**
  - 1st Class: **62.96%**
  - 2nd Class: **47.28%**
  - 3rd Class: **24.24%**
- **Observation:**
  1st Class passengers experienced the highest survival rate (**62.96%**), demonstrating a steep gradient of privilege and lifeboat access.

---

### Part K – Data Visualization

#### Task 23: Create Histograms for Numerical Features
- **Task:** What are we investigating?  
  Visualizing distributions for `Age`, `Fare`, `SibSp`, and `Parch`.
- **Code:**
  ```python
  numeric_cols = ["Age", "Fare", "SibSp", "Parch"]
  df[numeric_cols].hist(bins=30, figsize=(10, 6), layout=(2, 2), color="steelblue", edgecolor="black")
  plt.tight_layout()
  plt.savefig("plots/histograms_numerical.png", dpi=300)
  ```
- **Output:**
  Saved plot `plots/histograms_numerical.png`.
- **Observation (Student Questions):**
  1. *General age distribution:* Bell-shaped centered in the 20s to 30s, with a prominent peak at 28 due to median imputation.
  2. *Are Fare values evenly distributed?* No, highly right-skewed; most passengers paid under $50.
  3. *Did most passengers travel with many or few family members?* Most travelled alone or with very few family members (SibSp and Parch concentrated at 0).
  4. *Which numerical variable appears strongly skewed?* **Fare** exhibits severe right skewness, followed by **SibSp** and **Parch**.

---

### Part L – Univariate Analysis

#### Task 24: Detect Possible Outliers Using Boxplots
- **Task:** What are we investigating?  
  Identifying spread, medians, and outliers across numerical attributes.
- **Code:**
  ```python
  plt.figure(figsize=(8, 4))
  sns.boxplot(data=df[numeric_cols], palette="Set2")
  plt.title("Boxplots of Numerical Features")
  plt.savefig("plots/boxplots_numerical.png", dpi=300)
  ```
- **Output:**
  Saved plot `plots/boxplots_numerical.png`.
- **Observation (Student Questions):**
  1. *Which feature has the most obvious outliers?* **Fare** exhibits extreme outliers extending up to $512.33.
  2. *Does Fare contain unusually high observations?* Yes, several values far exceed the upper whisker.
  3. *Does seeing an outlier automatically mean the value is incorrect?* No. Outliers often represent genuine, valid real-world extremes. Here, they correspond to wealthy first-class passengers who purchased premier multi-room suites.

---

### Part M – Correlation Analysis

#### Task 25: Create a Correlation Matrix
- **Task:** What are we investigating?  
  Measuring pairwise linear relationships across numerical variables.
- **Code:**
  ```python
  selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]
  df[selected_cols].corr()
  ```
- **Output:**
  ```
            Age     SibSp     Parch    Pclass      Fare
  Age     1.000000 -0.233296 -0.172482 -0.339898  0.096688
  SibSp  -0.233296  1.000000  0.414838  0.083081  0.159651
  Parch  -0.172482  0.414838  1.000000  0.018443  0.216225
  Pclass -0.339898  0.083081  0.018443  1.000000 -0.549500
  Fare    0.096688  0.159651  0.216225 -0.549500  1.000000
  ```

#### Task 26: Display Correlation as a Heatmap
- **Task:** What are we investigating?  
  Rendering a color-coded heatmap to visually assess relationships.
- **Code:**
  ```python
  plt.figure(figsize=(8, 6))
  sns.heatmap(df[selected_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
  plt.title("Correlation Heatmap")
  plt.savefig("plots/correlation_heatmap.png", dpi=300)
  ```
- **Output:**
  Saved plot `plots/correlation_heatmap.png`.
- **Observation (Student Questions):**
  1. *Strongest positive correlation:* **SibSp and Parch** (+0.41), representing family members travelling together.
  2. *Variables showing negative correlation:* **Pclass and Fare** (-0.55), **Pclass and Age** (-0.34), **Age and SibSp** (-0.23), **Age and Parch** (-0.17).
  3. *Relationship between Pclass and Fare:* Strong negative correlation (-0.55); lower class number (1st Class) paid substantially higher fares.
  4. *Does correlation prove causation?* **No**, correlation measures statistical association, not cause-and-effect.

---

### Part N – Survival Visualization

#### Task 27: Compare Survival by Sex Using a Bar Plot
- **Task:** What are we investigating?  
  Visually evaluating survival proportion by gender.
- **Code:**
  ```python
  sns.barplot(x="Sex", y="Survived", data=df, hue="Sex", legend=False)
  plt.title("Sex vs Survival")
  plt.xlabel("Sex")
  plt.ylabel("Average Survival Rate")
  plt.savefig("plots/survival_by_sex.png", dpi=300)
  ```
- **Output:**
  Saved plot `plots/survival_by_sex.png`.
- **Observation (Conclusion on Sex and Survival):**
  Female passengers had a dramatically higher survival rate (~74.20%) than male passengers (~18.89%). This disparity was driven by the strict enforcement of the "women and children first" maritime evacuation protocol. Consequently, gender was the single most decisive factor influencing survival.

---

### Part O – Sorting and Finding Extreme Values

#### Task 28: Find the Five Highest-Paying Passengers
- **Task:** What are we investigating?  
  Sorting the dataset by fare in descending order and retrieving the top 5 records.
- **Code:**
  ```python
  topFares = df.sort_values(by="Fare", ascending=False)
  top5 = topFares.head(5)
  top5[["Name", "Sex", "Pclass", "Fare"]]
  ```
- **Output:**
  ```
                                     Name     Sex  Pclass      Fare
  679  Cardeza, Mr. Thomas Drake Martinez    male       1  512.3292
  258                    Ward, Miss. Anna  female       1  512.3292
  737              Lesurer, Mr. Gustave J    male       1  512.3292
  88           Fortune, Miss. Mabel Helen  female       1  263.0000
  438                   Fortune, Mr. Mark    male       1  263.0000
  ```

#### Task 29: Visualize the Five Highest-Paying Passengers
- **Task:** What are we investigating?  
  Generating a horizontal bar chart displaying names, fares, and gender of the top 5 paying passengers.
- **Code:**
  ```python
  plt.figure(figsize=(9, 5))
  sns.barplot(x="Fare", y="Name", data=top5, hue="Sex")
  plt.title("Five Highest-Paying Passengers")
  plt.xlabel("Fare ($)")
  plt.ylabel("Passenger Name")
  plt.savefig("plots/top5_highest_paying.png", dpi=300)
  ```
- **Output:**
  Saved plot `plots/top5_highest_paying.png`.
- **Observation (Student Questions):**
  1. *Who paid the highest fare?* Cardeza, Mr. Thomas Drake Martinez; Ward, Miss. Anna; and Lesurer, Mr. Gustave J (all paid **$512.33**).
  2. *What passenger class did they belong to?* **1st Class**.
  3. *Are their fares similar to the typical fare observed earlier?* No, they are dramatically higher than the median fare of **$14.45** and mean fare of **$32.20**.

---

# Part P – Final EDA Questions

1. **How many rows and columns are present in the dataset?**  
   The dataset contains **891 rows** and **12 columns**.

2. **Which columns contain missing values?**  
   `Age` (177 missing), `Cabin` (687 missing), and `Embarked` (2 missing).

3. **Which column contains the highest percentage of missing values?**  
   `Cabin` contains the highest percentage of missing values at **77.10%**.

4. **How were missing values in Age handled? Explain why the median was used.**  
   Missing values in `Age` were filled using the median age (**28.0 years**). The median is resistant to extreme values and outliers, making it a more reliable measure of central tendency than the mean for skewed distributions.

5. **How were missing values in Embarked handled? Explain why the mode is suitable for this feature.**  
   Missing values in `Embarked` were filled using the mode (**'S'**, Southampton). Because `Embarked` is categorical and over 72% of all passengers boarded at Southampton, the mode represents the most statistically probable value for the 2 missing records.

6. **Were duplicate rows found in the dataset?**  
   No duplicate rows were found in the dataset (`0 duplicate rows`).

7. **What is the overall survival rate?**  
   The overall survival rate was **38.38%** (342 survivors out of 891 passengers).

8. **Which sex had the higher survival rate?**  
   **Females** had a significantly higher survival rate (**74.20%**) than males (**18.89%**).

9. **Which passenger class had the highest survival rate?**  
   **1st Class** had the highest survival rate (**62.96%**), followed by 2nd Class (**47.28%**) and 3rd Class (**24.24%**).

10. **Which numerical feature shows the clearest extreme or outlier values?**  
    The **`Fare`** attribute shows the clearest extreme outlier values, with individual fares reaching **$512.33** compared to a median of **$14.45**.

11. **What do the Fare histograms and boxplots tell you about the distribution of ticket prices?**  
    They show that ticket prices are heavily right-skewed. The vast majority of travelers purchased low-cost tickets under $50, while a tiny luxury minority paid extreme premium prices.

12. **What relationship can you observe between passenger class and fare?**  
    There is a moderate-to-strong negative correlation (**-0.55**) between `Pclass` and `Fare`. Since lower numeric class codes denote superior accommodation (1 = 1st Class), passengers in higher classes paid significantly higher fares.

13. **Who were the five highest-paying passengers?**  
    1. Cardeza, Mr. Thomas Drake Martinez ($512.33, 1st Class, Male)  
    2. Ward, Miss. Anna ($512.33, 1st Class, Female)  
    3. Lesurer, Mr. Gustave J ($512.33, 1st Class, Male)  
    4. Fortune, Miss. Mabel Helen ($263.00, 1st Class, Female)  
    5. Fortune, Mr. Mark ($263.00, 1st Class, Male)

14. **Based on your complete EDA, mention three important findings from the Titanic dataset.**  
    1. *Gender Evacuation Protocol:* Female passengers had almost 4 times higher survival probability than males (74.20% vs. 18.89%) due to the "women and children first" maritime evacuation rule.  
    2. *Socioeconomic Gradient:* Passenger class strongly influenced survival outcomes (62.96% in 1st Class vs. 24.24% in 3rd Class), driven by proximity to the boat deck and rescue priority.  
    3. *Severe Economic Skew vs. Symmetric Age Demographic:* Fare distribution was heavily skewed with extreme luxury outliers up to $512.33, whereas passenger ages formed a bell-shaped distribution centered around young adulthood (median 28.0 years).

---

# Final Conclusion

The Titanic dataset consists of 891 passenger records across 12 features, containing key demographic, socioeconomic, and survival variables.
Missing data occurred primarily in Cabin (77.10%), Age (19.87%), and Embarked (0.22%), which were appropriately addressed by retaining Cabin without imputation, imputing Age with its median (28.0 years) to avoid outlier sensitivity, and imputing Embarked with its mode ('S').
Survival analysis clearly demonstrated that gender was the paramount predictor of survival (74.20% for females vs 18.89% for males), driven by the 'women and children first' maritime protocol.
Socioeconomic status was the second critical factor: 1st class passengers had a 62.96% survival rate compared to only 24.24% for 3rd class, reflecting lifeboat access disparities.
Numerical distributions revealed extreme right-skewness in Fare with genuine high-paying outliers up to $512.33, while Age exhibited a centered distribution around young adulthood.
Overall, this exploratory data analysis revealed the crucial social hierarchies that determined survival and provided the necessary data cleaning and feature insights for downstream predictive modeling.
