"""
Task 1: Exploratory Data Analysis on the Titanic Dataset
Comprehensive Script solving Tasks 1 to 29 according to the specification.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for generating figures cleanly
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure output directory for plots exists
PLOTS_DIR = os.path.join(os.path.dirname(__file__), "plots")
os.makedirs(PLOTS_DIR, exist_ok=True)

DATASET_PATH = os.path.join(os.path.dirname(__file__), "Titanic-Dataset.csv")
if not os.path.exists(DATASET_PATH):
    # Fallback to parent directory if not found in current folder
    DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "Titanic-Dataset.csv")

print("=" * 80)
print("TASK 1: Exploratory Data Analysis on the Titanic Dataset")
print("=" * 80)

# -----------------------------------------------------------------------------
# Part A - Setting Up Python
# Task 1: Import the Required Libraries
# -----------------------------------------------------------------------------
print("\n--- Part A: Setting Up Python ---")
print("Task 1: Libraries numpy, pandas, matplotlib.pyplot, seaborn successfully imported.")

# -----------------------------------------------------------------------------
# Part B - Loading the Dataset
# Task 2: Load the CSV File
# -----------------------------------------------------------------------------
print("\n--- Part B: Loading the Dataset ---")
print("Task 2: Loading dataset from:", DATASET_PATH)
df = pd.read_csv(DATASET_PATH)
print("Dataset successfully loaded into DataFrame `df`.")

# -----------------------------------------------------------------------------
# Part C - Initial Dataset Inspection
# Task 3: Display the First Few Rows
# Task 4: Display Random Records
# -----------------------------------------------------------------------------
print("\n--- Part C: Initial Dataset Inspection ---")
print("\nTask 3: Display First 5 Rows (df.head()):")
print(df.head())

print("\nTask 3: Display First 10 Rows (df.head(10)):")
print(df.head(10))

print("\n[Student Task - Task 3]:")
print("1. Target column: 'Survived' (indicates whether passenger survived: 0 = No, 1 = Yes)")
print("2. Numerical columns: PassengerId, Survived, Pclass, Age, SibSp, Parch, Fare")
print("3. Categorical / Text columns: Name, Sex, Ticket, Cabin, Embarked")

print("\nTask 4: Display 10 Random Records (df.sample(10)):")
sample_10 = df.sample(10, random_state=42)
print(sample_10)

print("\n[Student Task - Task 4]:")
print("Comparing sample records with first 5 rows: We observe missing values (NaN) clearly in columns such as 'Cabin' and 'Age'.")

# -----------------------------------------------------------------------------
# Part D - Understanding Dataset Structure
# Task 5: Display General Dataset Information
# Task 6: Find the Number of Rows and Columns
# Task 7: Check the Data Type of Every Column
# -----------------------------------------------------------------------------
print("\n--- Part D: Understanding Dataset Structure ---")
print("\nTask 5: General Dataset Information (df.info()):")
df.info()

print("\n[Student Questions - Task 5]:")
print("1. How many columns are present? ->", df.shape[1], "columns")
print("2. Which columns contain numerical data? -> PassengerId, Survived, Pclass, Age, SibSp, Parch, Fare")
print("3. Which columns contain text or categorical data? -> Name, Sex, Ticket, Cabin, Embarked")
print("4. Which columns appear to contain missing values? -> Age (714 non-null vs 891 total), Cabin (204 non-null), Embarked (889 non-null)")

print("\nTask 6: Dataset Shape (df.shape):")
rows, cols = df.shape
print(f"Number of rows = {rows}")
print(f"Number of columns = {cols}")

print("\nTask 7: Data Type of Every Column (df.dtypes):")
print(df.dtypes)

print("\n[Student Questions - Task 7]:")
print("• Integer columns: PassengerId, Survived, Pclass, SibSp, Parch (int64)")
print("• Float columns: Age, Fare (float64)")
print("• Object / text columns: Name, Sex, Ticket, Cabin, Embarked (object)")

# -----------------------------------------------------------------------------
# Part E - Missing and Duplicate Data
# Task 8: Count Non-Missing Values
# Task 9: Check Duplicate Rows
# -----------------------------------------------------------------------------
print("\n--- Part E: Missing and Duplicate Data ---")
print("\nTask 8: Count of Non-Missing Values per Column (df.notnull().sum()):")
print(df.notnull().sum())

print("\nTask 9: Check Duplicate Rows (df.duplicated().sum()):")
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)

print("\n[Student Question - Task 9]:")
print(f"Duplicate rows = {duplicate_count}")

# -----------------------------------------------------------------------------
# Part F - Understanding Unique Values
# Task 10: Check the Values of the Target Variable
# Task 11: Count Unique Values in Every Column
# -----------------------------------------------------------------------------
print("\n--- Part F: Understanding Unique Values ---")
print("\nTask 10: Unique Values in Target Variable 'Survived':")
target_uniques = df["Survived"].unique()
print(target_uniques)

print("\n[Student Question - Task 10]:")
print("What do the values 0 and 1 represent?")
print("• 0 represents passengers who did not survive (perished).")
print("• 1 represents passengers who survived.")

print("\nTask 11: Count Unique Values in Every Column (df.nunique()):")
print(df.nunique())

print("\n[Student Questions - Task 11]:")
print("1. Which columns contain very few unique values? -> Survived (2), Sex (2), Pclass (3), Embarked (3)")
print("2. Which columns appear to work as identifiers? -> PassengerId (891 unique values - unique primary key), Name (891), Ticket (681)")
print("3. Which columns may be categorical? -> Survived, Pclass, Sex, Embarked (as well as discrete family counts SibSp, Parch)")

# -----------------------------------------------------------------------------
# Part G - Statistical Summary
# Task 12: Generate Descriptive Statistics
# -----------------------------------------------------------------------------
print("\n--- Part G: Statistical Summary ---")
print("\nTask 12: Descriptive Statistics (df.describe()):")
desc = df.describe()
print(desc)

print("\n[Student Questions - Task 12]:")
print(f"1. Average passenger age: {desc.loc['mean', 'Age']:.2f} years")
print(f"2. Minimum passenger age: {desc.loc['min', 'Age']:.2f} years (infant ~5 months)")
print(f"3. Maximum passenger age: {desc.loc['max', 'Age']:.2f} years")
print(f"4. Average fare: ${desc.loc['mean', 'Fare']:.2f}")
print(f"5. Maximum fare: ${desc.loc['max', 'Fare']:.2f}")
print(f"6. Median age: {desc.loc['50%', 'Age']:.2f} years")

print("\n[Observations - Task 12]:")
print("1. The average age of passengers is approximately 29.70 years, with a median of 28.00 years, showing most passengers were young to middle-aged adults.")
print(f"2. Passenger fares range from ${desc.loc['min', 'Fare']:.2f} to ${desc.loc['max', 'Fare']:.2f}.")
print("3. The large difference between the median ($14.45) and maximum Fare ($512.33) indicates strong positive skewness, with high-fare outliers belonging to luxury first-class suites.")

# -----------------------------------------------------------------------------
# Part H - Detailed Missing-Value Analysis
# Task 13: Count Missing Values
# Task 14: Display Only Columns with Missing Values
# Task 15: Calculate Missing-Value Percentage
# -----------------------------------------------------------------------------
print("\n--- Part H: Detailed Missing-Value Analysis ---")
print("\nTask 13: Count Missing Values (df.isnull().sum()):")
missing_counts = df.isnull().sum()
print(missing_counts)

print("\nTask 14: Columns with Missing Values Sorted Descending:")
missing_sorted = missing_counts[missing_counts > 0].sort_values(ascending=False)
print(missing_sorted)

print("\n[Student Question - Task 14]:")
print(f"Which column contains the largest number of missing values? -> {missing_sorted.index[0]} ({missing_sorted.iloc[0]} missing)")

print("\nTask 15: Missing Value Count and Percentage Table:")
missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
missing_table = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage": missing_percentage
})
print(missing_table)

print("\n[Student Questions - Task 15]:")
print("1. Which column has the highest missing percentage? -> Cabin (77.10%)")
print("2. Is the missing percentage in Age small or significant? -> Significant (~19.87%, roughly 1 in 5 passengers). Dropping rows would discard valuable data, making median imputation necessary.")
print("3. Does Embarked contain many missing values? -> No, only 2 values (0.22%), which is negligible.")
print("4. Would filling Cabin be reliable if most values are missing? -> No. With over 77% data missing, imputing Cabin would inject excessive artificial noise and inaccurate assumptions.")

# -----------------------------------------------------------------------------
# Part I - Data Cleaning
# Task 16: Remove Duplicate Rows
# Task 17: Handle Missing Age Values
# Task 18: Handle Missing Embarked Values
# Task 19: Verify Missing Values After Cleaning
# -----------------------------------------------------------------------------
print("\n--- Part I: Data Cleaning ---")
print("\nTask 16: Remove Duplicate Rows:")
initial_len = len(df)
df = df.drop_duplicates().copy()
print(f"Rows before: {initial_len}, Rows after: {len(df)} (Duplicates removed: {initial_len - len(df)})")

print("\nTask 17: Handle Missing Age Values using Median:")
age_median = df["Age"].median()
print(f"Median Age: {age_median}")
df["Age"] = df["Age"].fillna(age_median)
print("Missing Age values filled with median.")

print("\nTask 18: Handle Missing Embarked Values using Mode:")
embarked_mode = df["Embarked"].mode()[0]
print(f"Mode Embarked: {embarked_mode}")
df["Embarked"] = df["Embarked"].fillna(embarked_mode)
print("Missing Embarked values filled with mode.")

print("\nTask 19: Verify Missing Values After Cleaning:")
post_clean_nulls = df.isnull().sum()
print(post_clean_nulls)

print("\n[Student Questions - Task 19]:")
print(f"1. Does Age still contain missing values? -> {df['Age'].isnull().sum() > 0} ({df['Age'].isnull().sum()} missing)")
print(f"2. Does Embarked still contain missing values? -> {df['Embarked'].isnull().sum() > 0} ({df['Embarked'].isnull().sum()} missing)")
print("3. Which column still contains a large number of missing values? -> Cabin (687 missing, kept unchanged per instructions)")

# -----------------------------------------------------------------------------
# Part J - Group-Level Analysis
# Task 20: Calculate the Overall Survival Rate
# Task 21: Compare Survival Rate by Sex
# Task 22: Compare Survival Rate by Passenger Class
# -----------------------------------------------------------------------------
print("\n--- Part J: Group-Level Analysis ---")
print("\nTask 20: Overall Survival Rate:")
survival_rate = df["Survived"].mean() * 100
print(f"Overall Survival Rate: {survival_rate:.2f}%")

print("\n[Student Task - Task 20]:")
print(f"Overall survival rate = {survival_rate:.2f} %")

print("\nTask 21: Compare Survival Rate by Sex:")
survival_by_sex = df.groupby("Sex")["Survived"].mean() * 100
print(survival_by_sex.round(2))

print("\n[Student Questions - Task 21]:")
print(f"1. Survival rate for females: {survival_by_sex['female']:.2f}%")
print(f"2. Survival rate for males: {survival_by_sex['male']:.2f}%")
print("3. Which group had the higher survival rate? -> Females")
print(f"4. Is the difference small or large? -> Extremely large (difference of {survival_by_sex['female'] - survival_by_sex['male']:.2f} percentage points, ~4x higher survival for females)")

print("\nTask 22: Compare Survival Rate by Passenger Class:")
survival_by_pclass = df.groupby("Pclass")["Survived"].mean() * 100
print(survival_by_pclass.round(2))

print("\n[Student Questions - Task 22]:")
print(f"1st Class = {survival_by_pclass[1]:.2f} %")
print(f"2nd Class = {survival_by_pclass[2]:.2f} %")
print(f"3rd Class = {survival_by_pclass[3]:.2f} %")
print("Which passenger class had the highest survival rate? -> 1st Class (62.96%)")

# -----------------------------------------------------------------------------
# Part K - Data Visualization
# Task 23: Create Histograms for Numerical Features
# -----------------------------------------------------------------------------
print("\n--- Part K: Data Visualization ---")
print("\nTask 23: Generating Histograms for Numerical Features...")
numeric_cols = ["Age", "Fare", "SibSp", "Parch"]
plt.figure()
df[numeric_cols].hist(
    bins=30,
    figsize=(10, 6),
    layout=(2, 2),
    color="steelblue",
    edgecolor="black"
)
plt.suptitle("Task 23: Histograms of Numerical Features", fontsize=14, y=1.02)
plt.tight_layout()
hist_path = os.path.join(PLOTS_DIR, "histograms_numerical.png")
plt.savefig(hist_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Histograms saved to: {hist_path}")

print("\n[Student Questions - Task 23]:")
print("1. General age distribution: Centered around late 20s to early 30s, displaying a bell-shaped distribution with a prominent central peak at 28 due to median imputation.")
print("2. Whether Fare values are evenly distributed: No, heavily right-skewed; the vast majority of fares are concentrated below $50.")
print("3. Whether most passengers travelled with many or few family members: Most travelled alone or with very few family members (SibSp and Parch are concentrated at 0).")
print("4. Which numerical variable appears strongly skewed: 'Fare' exhibits extreme right skewness, followed by 'SibSp' and 'Parch'.")

# -----------------------------------------------------------------------------
# Part L - Univariate Analysis
# Task 24: Detect Possible Outliers Using Boxplots
# -----------------------------------------------------------------------------
print("\n--- Part L: Univariate Analysis ---")
print("\nTask 24: Generating Boxplots for Outlier Detection...")
plt.figure(figsize=(8, 4))
sns.boxplot(data=df[numeric_cols], palette="Set2")
plt.title("Task 24: Boxplots of Numerical Features")
plt.ylabel("Value")
plt.tight_layout()
box_path = os.path.join(PLOTS_DIR, "boxplots_numerical.png")
plt.savefig(box_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Boxplots saved to: {box_path}")

print("\n[Student Questions - Task 24]:")
print("1. Which feature has the most obvious outliers? -> 'Fare' has the most extreme outliers, reaching up to $512.33.")
print("2. Does Fare contain unusually high observations? -> Yes, a handful of first-class tickets far exceed the typical upper whisker.")
print("3. Does seeing an outlier automatically mean the value is incorrect? Explain briefly:")
print("   -> No. Outliers can represent genuine, valid real-world extremes. In this case, the extreme fares correspond to legitimate wealthy first-class passengers who booked multi-room luxury suites.")

# -----------------------------------------------------------------------------
# Part M - Correlation Analysis
# Task 25: Create a Correlation Matrix
# Task 26: Display Correlation as a Heatmap
# -----------------------------------------------------------------------------
print("\n--- Part M: Correlation Analysis ---")
selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]
print("\nTask 25: Correlation Matrix:")
corr_matrix = df[selected_cols].corr()
print(corr_matrix.round(2))

print("\nTask 26: Generating Correlation Heatmap...")
plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1,
    linewidths=0.5
)
plt.title("Task 26: Correlation Heatmap")
plt.tight_layout()
heatmap_path = os.path.join(PLOTS_DIR, "correlation_heatmap.png")
plt.savefig(heatmap_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Heatmap saved to: {heatmap_path}")

print("\n[Student Questions - Task 26]:")
print("1. Which two features show the strongest positive correlation? -> SibSp and Parch (+0.41), representing family members travelling together.")
print("2. Which variables show a negative correlation? -> Pclass and Fare (-0.55), Pclass and Age (-0.34), Age and SibSp (-0.23), Age and Parch (-0.17).")
print("3. What relationship do you observe between Pclass and Fare? -> Strong negative correlation (-0.55), meaning 1st class (lower numerical value 1) is associated with much higher ticket fares, while 3rd class has lower fares.")
print("4. Does correlation prove that one variable causes another? -> No, correlation only measures linear association and direction, not direct causation.")

# -----------------------------------------------------------------------------
# Part N - Survival Visualization
# Task 27: Compare Survival by Sex Using a Bar Plot
# -----------------------------------------------------------------------------
print("\n--- Part N: Survival Visualization ---")
print("\nTask 27: Generating Survival by Sex Bar Plot...")
plt.figure(figsize=(6, 5))
sns.barplot(
    x="Sex",
    y="Survived",
    data=df,
    hue="Sex",
    legend=False,
    palette=["skyblue", "lightpink"]
)
plt.title("Task 27: Sex vs Survival")
plt.xlabel("Sex")
plt.ylabel("Average Survival Rate")
plt.tight_layout()
sex_bar_path = os.path.join(PLOTS_DIR, "survival_by_sex.png")
plt.savefig(sex_bar_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Survival by sex bar plot saved to: {sex_bar_path}")

print("\n[Student Question - Task 27]:")
print("Conclusion about sex and passenger survival:")
print("Female passengers had a significantly higher survival rate (~74.20%) compared to male passengers (~18.89%). This stark disparity reflects the strict enforcement of the maritime evacuation protocol 'women and children first'. Consequently, gender was one of the strongest single determinants of survival aboard the Titanic.")

# -----------------------------------------------------------------------------
# Part O - Sorting and Finding Extreme Values
# Task 28: Find the Five Highest-Paying Passengers
# Task 29: Visualize the Five Highest-Paying Passengers
# -----------------------------------------------------------------------------
print("\n--- Part O: Sorting and Finding Extreme Values ---")
print("\nTask 28: Five Highest-Paying Passengers:")
topFares = df.sort_values(by="Fare", ascending=False)
top5 = topFares.head(5)
print(top5[["Name", "Sex", "Pclass", "Fare"]])

print("\nTask 29: Generating Visualization for Five Highest-Paying Passengers...")
plt.figure(figsize=(9, 5))
sns.barplot(
    x="Fare",
    y="Name",
    data=top5,
    hue="Sex",
    palette={"female": "salmon", "male": "cornflowerblue"}
)
plt.title("Task 29: Five Highest-Paying Passengers")
plt.xlabel("Fare ($)")
plt.ylabel("Passenger Name")
plt.tight_layout()
top5_path = os.path.join(PLOTS_DIR, "top5_highest_paying.png")
plt.savefig(top5_path, dpi=300, bbox_inches="tight")
plt.close()
print(f"Top 5 highest paying passengers plot saved to: {top5_path}")

print("\n[Student Questions - Task 29]:")
print("1. Who paid the highest fare? -> Cardeza, Mr. Thomas Drake Martinez; Ward, Miss. Anna; and Lesurer, Mr. Gustave J (all paid $512.33).")
print("2. What passenger class did the highest-paying passengers belong to? -> 1st Class.")
print("3. Are their fares similar to the typical fare observed earlier? -> No, they are drastically higher than the median fare of $14.45 and mean fare of $32.20.")

# -----------------------------------------------------------------------------
# Summary of Final EDA Questions (Part P)
# -----------------------------------------------------------------------------
print("\n" + "=" * 80)
print("Part P - Final EDA Questions (Summary of Answers)")
print("=" * 80)
print("Q1. Rows and columns: 891 rows, 12 columns.")
print("Q2. Columns with missing values: Age (177), Cabin (687), Embarked (2).")
print("Q3. Column with highest percentage of missing values: Cabin (77.10%).")
print("Q4. Handling Age missing values: Replaced with median (28.0) because median is robust against outlier skewness.")
print("Q5. Handling Embarked missing values: Replaced with mode ('S') because Embarked is categorical and 'S' is overwhelmingly common.")
print(f"Q6. Duplicate rows: None found ({duplicate_count} duplicate rows).")
print(f"Q7. Overall survival rate: {survival_rate:.2f}%.")
print(f"Q8. Higher survival sex: Females (74.20% vs 18.89% for males).")
print(f"Q9. Highest survival passenger class: 1st Class (62.96%).")
print("Q10. Clearest extreme/outlier feature: 'Fare' (max $512.33 vs median $14.45).")
print("Q11. Fare distribution insights: Heavily right-skewed with most passengers paying modest amounts, and a small tail of luxury tickets.")
print("Q12. Class vs Fare relationship: Negative correlation (-0.55); higher socioeconomic class (1st class) paid markedly higher fares.")
print("Q13. Five highest-paying passengers: Cardeza, Mr. Thomas Drake Martinez; Ward, Miss. Anna; Lesurer, Mr. Gustave J; Fortune, Miss. Mabel Helen; Fortune, Mr. Mark.")
print("Q14. Three important findings:")
print("     1. Gender Priority: Female survival was nearly 4x that of males due to life-boat protocol.")
print("     2. Socioeconomic Disparity: 1st class passengers survived at 62.96%, whereas 3rd class survived at only 24.24%.")
print("     3. Data Skew & Outliers: Fares are heavily skewed with genuine luxury outliers up to $512.33, while Age follows a near-normal distribution around 28-30.")

print("\n" + "=" * 80)
print("FINAL CONCLUSION")
print("=" * 80)
print("""The Titanic dataset consists of 891 passenger records across 12 features, containing key demographic, socioeconomic, and survival variables.
Missing data occurred primarily in Cabin (77.10%), Age (19.87%), and Embarked (0.22%), which were appropriately addressed by retaining Cabin without imputation, imputing Age with its median (28.0 years) to avoid outlier sensitivity, and imputing Embarked with its mode ('S').
Survival analysis clearly demonstrated that gender was the paramount predictor of survival (74.20% for females vs 18.89% for males), driven by the 'women and children first' maritime protocol.
Socioeconomic status was the second critical factor: 1st class passengers had a 62.96% survival rate compared to only 24.24% for 3rd class, reflecting lifeboat access disparities.
Numerical distributions revealed extreme right-skewness in Fare with genuine high-paying outliers up to $512.33, while Age exhibited a centered distribution around young adulthood.
Overall, this exploratory data analysis revealed the crucial social hierarchies that determined survival and provided the necessary data cleaning and feature insights for downstream predictive modeling.""")

print("\nExecution completed successfully!")
