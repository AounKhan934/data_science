# Task 7: Check the Data Type of Every Column

## Task Description
**What are we investigating?**  
What type of data is stored in each column?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.dtypes)

```

## Output
```
PassengerId      int64
Survived         int64
Pclass           int64
Name               str
Sex                str
Age            float64
SibSp            int64
Parch            int64
Ticket             str
Fare           float64
Cabin              str
Embarked           str
dtype: object
```

## Observation
**What does the result tell us about the dataset?**  
The DataFrame contains 5 integer columns (int64), 2 decimal float columns (float64), and 5 string/text columns (object).

## Student Questions & Answers
- **Which columns are Integer?**  
  `PassengerId`, `Survived`, `Pclass`, `SibSp`, `Parch` (int64).
- **Which columns are Float?**  
  `Age`, `Fare` (float64).
- **Which columns are Object or text?**  
  `Name`, `Sex`, `Ticket`, `Cabin`, `Embarked` (object).
