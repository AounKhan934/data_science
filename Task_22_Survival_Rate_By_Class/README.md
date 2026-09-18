# Task 22: Compare Survival Rate by Passenger Class

## Task Description
**What are we investigating?**  
Was passenger class related to survival?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
rates = df.groupby("Pclass")["Survived"].mean() * 100
print(rates.round(2))

```

## Output
```
Pclass
1    62.96
2    47.28
3    24.24
Name: Survived, dtype: float64
```

## Observation
**What does the result tell us about the dataset?**  
Survival shows a steep socioeconomic gradient: 1st Class passengers survived at 62.96%, 2nd Class at 47.28%, and 3rd Class at only 24.24%.

## Student Questions & Answers
- **1st Class =**  
  62.96%
- **2nd Class =**  
  47.28%
- **3rd Class =**  
  24.24%
- **Which passenger class had the highest survival rate?**  
  1st Class (62.96%).
