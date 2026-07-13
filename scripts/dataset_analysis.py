import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("metadata/fashion_metadata.csv")

df["category"].value_counts().plot(kind="bar")

plt.savefig(
    "outputs/reports/category_distribution.png"
)

print("Chart Saved")