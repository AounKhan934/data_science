# Task 11: Count Unique Values in Every Column

## Task Description
**What are we investigating?**  
How many different values are present in each feature?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Number of unique values per column:")
print(df.nunique())

```

## Output
```
Number of unique values per column:
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

## Observation
**What does the result tell us about the dataset?**  
Columns with few unique values (`Survived`: 2, `Sex`: 2, `Pclass`: 3, `Embarked`: 3) represent categorical variables. `PassengerId` and `Name` have 891 unique values, acting as primary keys.

## Student Questions & Answers
- **1. Which columns contain very few unique values?**  
  `Survived` (2), `Sex` (2), `Pclass` (3), `Embarked` (3).
- **2. Which columns appear to work as identifiers?**  
  `PassengerId` (891 unique), `Name` (891 unique), `Ticket` (681 unique).
- **3. Which columns may be categorical?**  
  `Survived`, `Pclass`, `Sex`, `Embarked`.
