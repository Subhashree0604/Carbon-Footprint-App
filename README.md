# 🌍 Carbon Footprint Predictor

A **Streamlit web app** to estimate your annual CO₂ emissions based on your daily habits and provide personalized tips to reduce your carbon footprint.

---

## **Features**

1. **User Inputs**
   - Daily travel (km)
   - Electricity usage (kWh/day)
   - Diet type (veg, mixed, non-veg)
   - Preferred transport mode (public, bike, car)

2. **CO₂ Prediction**
   - Uses a trained machine learning model (`carbon_model.pkl`) to estimate annual CO₂ emissions in kilograms.

3. **CO₂ Breakdown**
   - Pie chart showing contributions from travel, electricity, diet, and transport.

4. **Recommendations & Personalized Tips**
   - Suggestions for reducing emissions based on inputs.
   - Tips are displayed in **colored boxes** with **emojis** for better UI.

5. **Modern UI**
   - Dark mode enabled
   - Colored info boxes and emojis
   - Card-style layout for tips and recommendations
