import pandas as pd
import os

# Input and output paths
input_path = os.path.join("data", "raw", "carbon_data.csv")
output_path = os.path.join("data", "processed", "cleaned_data.csv")

# 1️⃣ Load data
df = pd.read_csv("../data/carbon_data.csv")
print("Before cleaning:\n", df.head(), "\n")

# 2️⃣ Remove or fill missing values
# Fill numeric columns (like km or kWh) with their average
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col].fillna(df[col].mean())

# Fill text columns (like transport or diet) with “Unknown”
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna("Unknown")

# 3️⃣ Convert text to numbers for machine learning
df["transport"] = df["transport"].map({
    "car": 1, "bus": 0.5, "bike": 0.2, "walk": 0, "Unknown": 0.3
})
df["diet"] = df["diet"].map({
    "non-veg": 1, "veg": 0.5, "vegan": 0.2, "Unknown": 0.4
})

# 4️⃣ Check again for missing values
print("Missing values after cleaning:\n", df.isnull().sum(), "\n")

# 5️⃣ Save cleaned data
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)
print("✅ Cleaned data saved to data/processed/cleaned_data.csv")

# -------------------------------
# Step 5: Feature Engineering
# -------------------------------

# 1. Annual electricity usage
df["annual_energy_kwh"] = df["electricity_kwh_per_day"] * 365

# 2. Transport emission calculation
# Simple transport emission feature using numeric encoded transport
df["transport_emission"] = df["travel_km_per_day"] * df["transport"]


# 3. Diet score
diet_map = {
    "vegan": 1,
    "vegetarian": 2,
    "mixed": 3,
    "non-veg": 4
}

# Ensure diet is string
df["diet"] = df["diet"].astype(str)

# Map diet score safely
df["diet_score"] = df["diet"].str.lower().map({
    "veg": 1,
    "non-veg": 3,
    "vegan": 0
}).fillna(2)   # default score

# 4. Daily CO2 estimation
df["daily_co2_estimate"] = df["total_co2_kg_per_year"] / 365
