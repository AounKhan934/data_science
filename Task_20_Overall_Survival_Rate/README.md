# Task 20: Calculate the Overall Survival Rate

## Task Description
**What are we investigating?**  
What percentage of Titanic passengers survived?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
survival_rate = df["Survived"].mean() * 100
print(f"Overall Survival Rate: {survival_rate:.2f}%")

```

## Output
```
Overall Survival Rate: 38.38%
```

## Observation
**What does the result tell us about the dataset?**  
The overall survival rate was 38.38%, meaning only approximately 38 out of every 100 passengers survived the disaster.

## Student Questions & Answers
- **Overall survival rate =**  
  38.38%
- **Why does mean work here?**  
  Since `Survived` is encoded as 0 and 1, the arithmetic mean equals the proportion of 1s (survivors).
