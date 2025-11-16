import matplotlib.pyplot as plt
import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/carbon_model.pkl")

st.title("🌍 Carbon Footprint Predictor")
st.write("Enter your daily habits to estimate your yearly CO₂ emissions.")

# -------------------------
# USER INPUTS
# -------------------------

# Travel (km)
travel = st.number_input("Daily Travel (km)", min_value=0.0, value=10.0)

# Electricity (kWh)
electricity = st.number_input("Daily Electricity Usage (kWh)", min_value=0.0, value=5.0)

# Diet input
diet = st.selectbox("Select your diet type:", ["veg", "mixed", "non-veg"])

# Convert diet to numeric
if diet == "veg":
    diet_code = 0
elif diet == "mixed":
    diet_code = 1
else:
    diet_code = 2  # non-veg

# Transport input
transport = st.selectbox("Preferred Transport Mode:", ["public", "bike", "car"])

# Convert transport to numeric
if transport == "public":
    transport_code = 0
elif transport == "bike":
    transport_code = 1
else:
    transport_code = 2  # car

# -------------------------
# PREDICTION
# -------------------------

if st.button("Predict CO₂ Emissions"):
    # Build input row (column names match model)
    data = pd.DataFrame([{
        "travel_km_per_day": travel,
        "electricity_kwh_per_day": electricity,
        "diet": diet_code,
        "transport": transport_code
    }])

    # Predict
    prediction = model.predict(data)[0]

    st.success(f"🌱 **Estimated Annual CO₂:** {prediction:.2f} kg")

    # -------------------------
    # PIE CHART FOR CO₂ BREAKDOWN
    # -------------------------

    # Approx emission factors (example logic)
    travel_emission = travel * 365 * 0.21
    electricity_emission = electricity * 365 * 0.50
    diet_emission = (diet_code + 1) * 100
    transport_emission = (transport_code + 1) * 80

    labels = ["Travel", "Electricity", "Diet", "Transport"]
    values = [travel_emission, electricity_emission, diet_emission, transport_emission]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")

    st.subheader("📊 CO₂ Emission Breakdown")
    st.pyplot(fig)

    # -------------------------
    # RECOMMENDATIONS
    # -------------------------
    st.subheader("💡 Suggestions to Reduce Emissions")

    # Travel recommendation
    if travel > 20:
        st.write("🚗 *Try to reduce long travel distances. Consider carpooling or public transport!*")
    else:
        st.write("🚶 *Your travel emissions are low — good job!*")

    # Electricity recommendation
    if electricity > 8:
        st.write("💡 *You can save energy by using LED bulbs or reducing AC usage.*")
    else:
        st.write("🔌 *Your electricity use is moderate.*")

    # Diet recommendation
    if diet_code == 2:
        st.write("🍗 *Non-veg diet produces more CO₂. Try including more plant-based meals.*")
    elif diet_code == 1:
        st.write("🥗 *Mixed diet — balanced, but can improve with more veg meals.*")
    else:
        st.write("🌿 *Veg diet is great for reducing carbon footprint!*")

    # Transport recommendation
    if transport_code == 2:
        st.write("🚘 *Cars emit the most. Switching to public transport will help the planet!*")
    elif transport_code == 1:
        st.write("🚲 *Bike transport is eco-friendly — great choice!*")
    else:
        st.write("🚌 *Public transport greatly reduces carbon emissions!*")

    # -------------------------
    # PERSONALIZED TIPS
    # -------------------------
    st.subheader("🌿 Personalized Tips for You")

    def get_personalized_tips(electricity, diet_code, travel):
        tips = []

        if electricity > 10:
            tips.append("⚡ Switch to 5-star appliances to save energy.")

        if diet_code == 2:  # Non-veg
            tips.append("🥩 Reducing red meat can cut up to 800 kg CO₂/year.")

        if travel > 20:
            tips.append("🚗 Try weekly WFH or carpool groups to reduce travel emissions.")

        return tips

    tips = get_personalized_tips(electricity, diet_code, travel)

    if tips:
        for tip in tips:
            st.info(tip)
    else:
        st.success("👏 Your habits are already eco-friendly!")
