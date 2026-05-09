import pandas as pd

# -----------------------------
# EXTRACT
# -----------------------------
print("Extract Phase")

df = pd.read_csv("SampleSuperstore.csv")

print(df.head())

# -----------------------------
# TRANSFORM
# -----------------------------
print("\nTransform Phase")

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna(0)

# Create Profit Ratio column
df["Profit_Ratio"] = (df["Profit"] / df["Sales"]) * 100

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract Year
df["Order_Year"] = df["Order Date"].dt.year

# Filter positive sales
df = df[df["Sales"] > 0]

print(df.head())

# -----------------------------
# LOAD
# -----------------------------
print("\nLoad Phase")

df.to_csv("Cleaned_Superstore.csv", index=False)

print("Cleaned dataset saved successfully")