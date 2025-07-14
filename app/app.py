# app/app.py

import streamlit as st
from recommendation import recommend_crops

st.set_page_config(page_title="KrishiMitra AI", layout="centered")

st.title("🌱 KrishiMitra AI")
st.write("A smart crop recommendation system for Indian farmers.")

# User input form
with st.form("input_form"):
    location = st.text_input("Enter your PIN code or GPS coordinates:")
    land_size = st.number_input("Enter land size (acres):", min_value=0.1)
    budget = st.selectbox("Select your budget level:", ["Low", "Medium", "High"])
    submit = st.form_submit_button("Get Recommendations")

if submit:
    if location and land_size:
        recommendations = recommend_crops(location, land_size, budget)
        st.success("Recommended Crops:")
        for idx, crop in enumerate(recommendations, start=1):
            st.write(f"✅ **{idx}. {crop['name']}**")
            st.write(f"ROI: {crop['roi']}% | Resilience: {crop['resilience']} | Sowing window: {crop['sowing_window']}")
    else:
        st.error("Please fill all the fields.")
