import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import os

# Load cleaned data
data_path = os.path.join("data", "processed", "cleaned_data.csv")
df = pd.read_csv(data_path)

# Handle NaN
df = df.dropna()

# NEW: Add diet + transport features
X = df[["travel_km_per_day", "electricity_kwh_per_day", "diet", "transport"]]
y = df["total_co2_kg_per_year"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("R2:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# Save model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/carbon_model.pkl")

print("Model saved successfully!")
