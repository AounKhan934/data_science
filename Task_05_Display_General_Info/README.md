# Task 5: Display General Dataset Information

## Task Description
**What are we investigating?**  
How many columns are present, what are their data types, and which columns contain missing values?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
df.info()

```

## Output
```
<class 'pandas.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype  
---  ------       --------------  -----  
 0   PassengerId  891 non-null    int64  
 1   Survived     891 non-null    int64  
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object 
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object 
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object 
 11  Embarked     889 non-null    object 
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
```

## Observation
**What does the result tell us about the dataset?**  
The dataset occupies 83.7+ KB of memory. 9 out of 12 columns are completely populated with 891 values, while Age, Cabin, and Embarked have missing entries.

## Student Questions & Answers
- **1. How many columns are present?**  
  12 columns.
- **2. Which columns contain numerical data?**  
  `PassengerId`, `Survived`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`.
- **3. Which columns contain text or categorical data?**  
  `Name`, `Sex`, `Ticket`, `Cabin`, `Embarked`.
- **4. Which columns appear to contain missing values?**  
  `Age` (714 non-null), `Cabin` (204 non-null), and `Embarked` (889 non-null).
