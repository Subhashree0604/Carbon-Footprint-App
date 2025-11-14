import pandas as pd

# 1️⃣ Load your dataset (make sure file name matches your data)
df = pd.read_csv("../data/carbon_data.csv")

# 2️⃣ Show first 5 rows
print("\n🔹 First 5 rows of your data:")
print(df.head())

# 3️⃣ Summary statistics
print("\n🔹 Summary of numbers:")
print(df.describe())

# 4️⃣ Check for missing values
print("\n🔹 Missing values:")
print(df.isnull().sum())
