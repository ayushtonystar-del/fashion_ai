import pandas as pd
import json

df = pd.read_csv(
    "metadata/fashion_metadata.csv"
)

knowledge = []

for _, row in df.iterrows():

    knowledge.append({

        "id": str(_),

        "image": row["image"],

        "category": row["category"],

        "color": row["color"],

        "material": row["material"],

        "style": row["style"],

        "description":
        f"{row['color']} {row['material']} "
        f"{row['style']} {row['category']}"

    })

with open(
    "metadata/fashion_knowledge.json",
    "w"
) as f:

    json.dump(
        knowledge,
        f,
        indent=4
    )

print("Knowledge Base Created")