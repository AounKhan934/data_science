# Task 25: Create a Correlation Matrix

## Task Description
**What are we investigating?**  
Are numerical variables related to one another?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]
print(df[selected_cols].corr().round(2))

```

## Output
```
         Age  SibSp  Parch  Pclass  Fare
Age     1.00  -0.31  -0.19   -0.37  0.10
SibSp  -0.31   1.00   0.41    0.08  0.16
Parch  -0.19   0.41   1.00    0.02  0.22
Pclass -0.37   0.08   0.02    1.00 -0.55
Fare    0.10   0.16   0.22   -0.55  1.00
```

## Observation
**What does the result tell us about the dataset?**  
Correlation analysis shows moderate negative correlation between `Pclass` and `Fare` (-0.55), and positive correlation between `SibSp` and `Parch` (+0.41).

## Student Questions & Answers
- **What do correlation values mean?**  
  +1 means strong positive linear relationship, -1 means strong negative relationship, 0 means no linear relationship.
