# Task 6: Find the Number of Rows and Columns

## Task Description
**What are we investigating?**  
What is the exact size of our dataset?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
rows, columns = df.shape
print(f"Number of rows = {rows}")
print(f"Number of columns = {columns}")

```

## Output
```
Number of rows = 891
Number of columns = 12
```

## Observation
**What does the result tell us about the dataset?**  
The dataset contains 891 passenger records and 12 attributes.

## Student Questions & Answers
- **Number of rows =**  
  891
- **Number of columns =**  
  12
