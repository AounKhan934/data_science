# Task 3: Display the First Few Rows

## Task Description
**What are we investigating?**  
What does the dataset look like at first glance?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("First 5 rows:")
print(df.head())

print("\nFirst 10 rows:")
print(df.head(10))

```

## Output
```
First 5 rows:
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S

[5 rows x 12 columns]

First 10 rows:
   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
1            2         1       1  ...  71.2833   C85         C
2            3         1       3  ...   7.9250   NaN         S
3            4         1       1  ...  53.1000  C123         S
4            5         0       3  ...   8.0500   NaN         S
5            6         0       3  ...   8.4583   NaN         Q
6            7         0       1  ...  51.8625   E46         S
7            8         0       3  ...  21.0750   NaN         S
8            9         1       3  ...  11.1333   NaN         S
9           10         1       2  ...  30.0708   NaN         C

[10 rows x 12 columns]
```

## Observation
**What does the result tell us about the dataset?**  
Inspecting the first rows reveals passenger identification, survival status, cabin classes, full names, ages, ticket identifiers, fares, and ports of embarkation.

## Student Questions & Answers
- **1. The target column:**  
  `Survived` (binary outcome: 0 = Did not survive, 1 = Survived).
- **2. Numerical columns:**  
  `PassengerId`, `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`.
- **3. Categorical or text columns:**  
  `Name`, `Sex`, `Ticket`, `Cabin`, `Embarked`.
