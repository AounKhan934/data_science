# Task 12: Generate Descriptive Statistics

## Task Description
**What are we investigating?**  
What are the basic statistical properties of the numerical columns?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
print(df.describe())

```

## Output
```
       PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200

[8 rows x 7 columns]
```

## Observation
**What does the result tell us about the dataset?**  
The average age of passengers is approximately 29.70 years (median 28.0). Passenger fares range from $0.00 to $512.33. The large gap between median ($14.45) and max fare ($512.33) indicates positive skewness with high-cost luxury outliers.

## Student Questions & Answers
- **1. Average passenger age:**  
  29.70 years
- **2. Minimum passenger age:**  
  0.42 years (~5 months)
- **3. Maximum passenger age:**  
  80.00 years
- **4. Average fare:**  
  $32.20
- **5. Maximum fare:**  
  $512.33
- **6. Median age:**  
  28.00 years
