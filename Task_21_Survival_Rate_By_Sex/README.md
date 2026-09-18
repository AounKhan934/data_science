# Task 21: Compare Survival Rate by Sex

## Task Description
**What are we investigating?**  
Did male and female passengers have similar survival rates?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
rates = df.groupby("Sex")["Survived"].mean() * 100
print(rates.round(2))

```

## Output
```
Sex
female    74.20
male      18.89
Name: Survived, dtype: float64
```

## Observation
**What does the result tell us about the dataset?**  
Female passengers survived at a rate of 74.20%, whereas male passengers survived at only 18.89% (~4x difference).

## Student Questions & Answers
- **1. What was the survival rate for females?**  
  74.20%
- **2. What was the survival rate for males?**  
  18.89%
- **3. Which group had higher survival rate?**  
  Females
- **4. Is the difference small or large?**  
  Extremely large (difference of 55.31 percentage points).
