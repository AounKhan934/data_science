# Task 28: Find the Five Highest-Paying Passengers

## Task Description
**What are we investigating?**  
Which passengers paid the highest fares?

## Code
```python
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")
topFares = df.sort_values(by="Fare", ascending=False)
top5 = topFares.head(5)
print(top5[["Name", "Sex", "Pclass", "Fare"]])

```

## Output
```
                                   Name     Sex  Pclass      Fare
679  Cardeza, Mr. Thomas Drake Martinez    male       1  512.3292
258                    Ward, Miss. Anna  female       1  512.3292
737              Lesurer, Mr. Gustave J    male       1  512.3292
88           Fortune, Miss. Mabel Helen  female       1  263.0000
438                   Fortune, Mr. Mark    male       1  263.0000
```

## Observation
**What does the result tell us about the dataset?**  
The top 3 passengers paid an identical record fare of $512.33, followed by the Fortune family who paid $263.00. All were in 1st Class.

## Student Questions & Answers
- **What does `ascending=False` mean?**  
  Sorts records from largest value to smallest value.
