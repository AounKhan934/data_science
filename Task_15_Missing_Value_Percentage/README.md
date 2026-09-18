# Task 15: Calculate Missing-Value Percentage

## Task Description
**What are we investigating?**  
What percentage of each column is missing?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
table = pd.DataFrame({
    "Missing Count": df.isnull().sum(),
    "Missing Percentage": missing_percentage
})
print(table)

```

## Output
```
             Missing Count  Missing Percentage
PassengerId              0                0.00
Survived                 0                0.00
Pclass                   0                0.00
Name                     0                0.00
Sex                      0                0.00
Age                    177               19.87
SibSp                    0                0.00
Parch                    0                0.00
Ticket                   0                0.00
Fare                     0                0.00
Cabin                  687               77.10
Embarked                 2                0.22
```

## Observation
**What does the result tell us about the dataset?**  
`Cabin` is missing 77.10% of its data, `Age` is missing 19.87%, and `Embarked` is missing 0.22%.

## Student Questions & Answers
- **1. Which column has highest missing percentage?**  
  `Cabin` (77.10%).
- **2. Is the missing percentage in Age small or significant?**  
  Significant (~19.87%, ~1 in 5 passengers). Dropping rows would discard 20% of the dataset, making imputation necessary.
- **3. Does Embarked contain many missing values?**  
  No, only 2 missing entries (0.22%), which is negligible.
- **4. Would filling Cabin be reliable if most values are missing?**  
  No, because over 77% of entries are absent. Imputation would introduce artificial noise and false patterns.
