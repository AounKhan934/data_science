"""
Task 26: Display Correlation as a Heatmap
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")
selected_cols = ["Age", "SibSp", "Parch", "Pclass", "Fare"]

plt.figure(figsize=(8, 6))
sns.heatmap(
    df[selected_cols].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png", dpi=300)
plt.show()
