# Task 4: Display Random Records

## Task Description
**What are we investigating?**  
Do different parts of the dataset contain similar types of records, and are there missing values?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print("10 Random Records:")
print(df.sample(10, random_state=42))

```

## Output
```
10 Random Records:
     PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
709          710         1       3  ...  15.2458   NaN         C
439          440         0       2  ...  10.5000   NaN         S
840          841         0       3  ...   7.9250   NaN         S
720          721         1       2  ...  33.0000   NaN         S
39            40         1       3  ...  11.2417   NaN         C
290          291         1       1  ...  78.8500   NaN         S
300          301         1       3  ...   7.7500   NaN         Q
333          334         0       3  ...  18.0000   NaN         S
208          209         1       3  ...   7.7500   NaN         Q
136          137         1       1  ...  26.2833   D47         S

[10 rows x 12 columns]
```

## Observation
**What does the result tell us about the dataset?**  
Random rows confirm consistent data structures across different portions of the dataset while revealing missing values (`NaN`) in the `Cabin` and `Age` columns.

## Student Questions & Answers
- **Compare the random rows with the first five rows:**  
  Random sampling avoids ordering bias present at the head of the file and exposes missing values (`NaN`) in `Cabin` and `Age` across diverse passenger classes.
