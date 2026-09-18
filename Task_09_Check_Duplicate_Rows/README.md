# Task 9: Check Duplicate Rows

## Task Description
**What are we investigating?**  
Does the dataset contain exactly repeated records?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
duplicate_count = df.duplicated().sum()
print("Duplicate Rows:", duplicate_count)

```

## Output
```
Duplicate Rows: 0
```

## Observation
**What does the result tell us about the dataset?**  
There are zero duplicated rows in the dataset; all 891 entries are distinct observations.

## Student Questions & Answers
- **How many duplicate rows are present?**  
  Duplicate rows = 0
