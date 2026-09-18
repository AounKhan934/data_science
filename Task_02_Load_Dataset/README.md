# Task 2: Load the CSV File

## Task Description
**What are we investigating?**  
How can we bring the dataset into Python so that we can analyze it?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("Dataset loaded successfully.")
print(f"Dimensions: {df.shape[0]} rows, {df.shape[1]} columns")

```

## Output
```
Dataset loaded successfully.
Dimensions: 891 rows, 12 columns
```

## Observation
**What does the result tell us about the dataset?**  
The CSV dataset is parsed into a structured 2D Pandas DataFrame consisting of 891 records and 12 columns.

## Student Questions & Answers
- **What function is used to load a CSV in Pandas?**  
  `pd.read_csv('filename.csv')` reads a CSV file and converts it into a DataFrame.
- **What is a DataFrame?**  
  A 2-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table.
