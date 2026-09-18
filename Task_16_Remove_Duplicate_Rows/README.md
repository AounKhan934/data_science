# Task 16: Remove Duplicate Rows

## Task Description
**What are we investigating?**  
Remove any duplicate records to guarantee data uniqueness.

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
initial_count = len(df)
df = df.drop_duplicates().copy()
print(f"Initial rows: {initial_count}, Rows after drop_duplicates: {len(df)}")

```

## Output
```
Initial rows: 891, Rows after drop_duplicates: 891
```

## Observation
**What does the result tell us about the dataset?**  
Executing `drop_duplicates()` confirms that 0 duplicates existed, retaining all 891 unique passenger records.

## Student Questions & Answers
- **Why use `.copy()`?**  
  `.copy()` creates an independent copy in memory so future modifications do not raise SettingWithCopy warnings.
