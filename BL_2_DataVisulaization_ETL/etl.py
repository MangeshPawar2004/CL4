import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# EXTRACT
# -----------------------------
print("Extract Phase")

df = pd.read_csv("titanic.csv")

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# -----------------------------
# TRANSFORM
# -----------------------------
print("\nTransform Phase")

# Check null values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Embarked missing values
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Remove duplicates
df = df.drop_duplicates()

# Create Age Group Column
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 19, 35, 60, 100],
    labels=["Child", "Teen", "Young", "Adult", "Senior"]
)

print("\nTransformed Data:")
print(df.head())

# -----------------------------
# LOAD
# -----------------------------
print("\nLoad Phase")

df.to_csv("cleaned_titanic.csv", index=False)

print("Cleaned dataset saved as cleaned_titanic.csv")

# -----------------------------
# DATA VISUALIZATION
# -----------------------------

sns.set(style="whitegrid")

# -----------------------------------------
# 1. Survival Count
# -----------------------------------------
plt.figure(figsize=(6,5))
sns.countplot(x="Survived", data=df)

plt.title("Survival Count")
plt.show()

# -----------------------------------------
# 2. Survival by Gender
# -----------------------------------------
plt.figure(figsize=(6,5))
sns.countplot(x="Sex", hue="Survived", data=df)

plt.title("Survival by Gender")
plt.show()

# -----------------------------------------
# 3. Passenger Class Distribution
# -----------------------------------------
plt.figure(figsize=(6,5))
sns.countplot(x="Pclass", data=df)

plt.title("Passenger Class Distribution")
plt.show()

# -----------------------------------------
# 4. Age Distribution
# -----------------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=20, kde=True)

plt.title("Age Distribution")
plt.show()

# -----------------------------------------
# 5. Fare Distribution
# -----------------------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["Fare"], bins=20, kde=True)

plt.title("Fare Distribution")
plt.show()

# -----------------------------------------
# 6. Survival by Passenger Class
# -----------------------------------------
plt.figure(figsize=(7,5))
sns.countplot(x="Pclass", hue="Survived", data=df)

plt.title("Survival by Passenger Class")
plt.show()

# -----------------------------------------
# 7. Age Group Distribution
# -----------------------------------------
plt.figure(figsize=(8,5))
sns.countplot(x="AgeGroup", data=df)

plt.title("Age Group Distribution")
plt.show()