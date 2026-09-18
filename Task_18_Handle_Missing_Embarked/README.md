# Task 18: Handle Missing Embarked Values

## Task Description
**What are we investigating?**  
How can missing categorical values in Embarked be filled?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
mode_embarked = df["Embarked"].mode()[0]
print(f"Most common embarkation port (mode): {mode_embarked}")

df["Embarked"] = df["Embarked"].fillna(mode_embarked)
print("Remaining missing values in Embarked:", df["Embarked"].isnull().sum())

```

## Output
```
Most common embarkation port (mode): S
Remaining missing values in Embarked: 0
```

## Observation
**What does the result tell us about the dataset?**  
The 2 missing embarkation ports were imputed with the statistical mode ('S' for Southampton), which accounts for over 72% of all boarding passengers.

## Student Questions & Answers
- **Why use mode for categorical variables?**  
  The mode gives the most frequently observed category, making it the most statistically probable value.
- **Why `[0]`?**  
  `mode()` returns a Pandas Series because there can be ties; `[0]` selects the primary mode.
