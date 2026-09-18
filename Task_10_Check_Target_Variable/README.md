# Task 10: Check the Values of the Target Variable

## Task Description
**What are we investigating?**  
What values are used to represent survival?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Unique values in 'Survived':", df["Survived"].unique())

```

## Output
```
Unique values in 'Survived': [0 1]
```

## Observation
**What does the result tell us about the dataset?**  
Survival is encoded as binary integers: 0 and 1.

## Student Questions & Answers
- **What do the values 0 and 1 represent?**  
  0 = Passenger did not survive (died); 1 = Passenger survived.
