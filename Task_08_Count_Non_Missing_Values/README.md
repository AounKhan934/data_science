# Task 8: Count Non-Missing Values

## Task Description
**What are we investigating?**  
How many valid, non-null values are available in each column?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Non-missing values per column:")
print(df.notnull().sum())

```

## Output
```
Non-missing values per column:
PassengerId    891
Survived       891
Pclass         891
Name           891
Sex            891
Age            714
SibSp          891
Parch          891
Ticket         891
Fare           891
Cabin          204
Embarked       889
dtype: int64
```

## Observation
**What does the result tell us about the dataset?**  
`notnull().sum()` confirms that most columns have complete data (891 values), while `Age` has 714, `Cabin` has 204, and `Embarked` has 889 valid values.

## Student Questions & Answers
- **What does `notnull()` do?**  
  Returns a boolean DataFrame with `True` where values exist and `False` where missing.
- **What does `sum()` do on boolean Series?**  
  Sums `True` values (treating True as 1), giving the count of available entries.
