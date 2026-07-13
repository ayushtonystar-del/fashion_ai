import pandas as pd

# Step 1: Load metadata
df = pd.read_csv("fashion_metadata.csv")

# Step 2: Check columns
print(df.columns)

# Step 3: Create structured fashion records
fashion_records = []

for _, row in df.iterrows():

    fashion_records.append({
        "image": row["image"],
        "category": row["category"],
        "color": row["color"],
        "material": row["material"],
        "style": row["style"]
    })

# Step 4: Verify output
print(fashion_records[:5])