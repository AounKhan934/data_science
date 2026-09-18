"""
Task 29: Visualize the Five Highest-Paying Passengers
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")
top5 = df.sort_values(by="Fare", ascending=False).head(5)

plt.figure(figsize=(9, 5))
sns.barplot(
    x="Fare",
    y="Name",
    data=top5,
    hue="Sex",
    palette={"female": "salmon", "male": "cornflowerblue"}
)
plt.title("Five Highest-Paying Passengers")
plt.xlabel("Fare ($)")
plt.ylabel("Passenger Name")
plt.tight_layout()
plt.savefig("top5_highest_paying.png", dpi=300)
plt.show()
