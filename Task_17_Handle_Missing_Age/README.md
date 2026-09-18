# Task 17: Handle Missing Age Values

## Task Description
**What are we investigating?**  
How should missing numerical values in Age be handled?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
median_age = df["Age"].median()
print(f"Median Age: {median_age}")

df["Age"] = df["Age"].fillna(median_age)
print("Remaining missing values in Age:", df["Age"].isnull().sum())

```

## Output
```
Median Age: 28.0
Remaining missing values in Age: 0
```

## Observation
**What does the result tell us about the dataset?**  
Missing age values were replaced with the median age (28.0 years). The median is preferred over the mean because it is less affected by extreme values and outliers.

## Student Questions & Answers
- **Why use Median instead of Mean?**  
  The median represents the 50th percentile and is robust against skewed values and outliers, unlike the mean.
