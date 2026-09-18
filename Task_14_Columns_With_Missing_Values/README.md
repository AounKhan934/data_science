# Task 14: Display Only Columns with Missing Values

## Task Description
**What are we investigating?**  
Which columns have missing data, sorted from highest to lowest?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
missing_values = df.isnull().sum()
print(missing_values[missing_values > 0].sort_values(ascending=False))

```

## Output
```
Cabin       687
Age         177
Embarked      2
dtype: int64
```

## Observation
**What does the result tell us about the dataset?**  
Sorting reveals that missingness is overwhelmingly concentrated in `Cabin` (687), followed by `Age` (177), while `Embarked` has only 2 missing entries.

## Student Questions & Answers
- **Which column contains the largest number of missing values?**  
  `Cabin` with 687 missing values.
