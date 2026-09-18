# Task 19: Verify Missing Values After Cleaning

## Task Description
**What are we investigating?**  
Did our cleaning operations succeed in resolving missing data?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("Missing values after cleaning:")
print(df.isnull().sum())

```

## Output
```
Missing values after cleaning:
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age              0
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         0
dtype: int64
```

## Observation
**What does the result tell us about the dataset?**  
`Age` and `Embarked` now have 0 missing entries. `Cabin` intentionally remains with 687 missing values per the instructions.

## Student Questions & Answers
- **1. Does Age still contain missing values?**  
  No (0 missing).
- **2. Does Embarked still contain missing values?**  
  No (0 missing).
- **3. Which column still contains a large number of missing values?**  
  `Cabin` (687 missing).
