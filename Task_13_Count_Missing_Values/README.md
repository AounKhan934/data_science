# Task 13: Count Missing Values

## Task Description
**What are we investigating?**  
Which columns contain missing data, and how many values are missing?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Missing values per column:")
print(df.isnull().sum())

```

## Output
```
Missing values per column:
PassengerId      0
Survived         0
Pclass           0
Name             0
Sex              0
Age            177
SibSp            0
Parch            0
Ticket           0
Fare             0
Cabin          687
Embarked         2
dtype: int64
```

## Observation
**What does the result tell us about the dataset?**  
Three features have missing values: `Cabin` has 687 missing, `Age` has 177 missing, and `Embarked` has 2 missing. All other 9 columns are complete.

## Student Questions & Answers
- **Which columns contain missing values?**  
  `Cabin` (687), `Age` (177), and `Embarked` (2).
