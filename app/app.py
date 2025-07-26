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
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
from datetime import datetime
from recommendation import get_crop_recommendations
from data_preprocessing import preprocess_user_input

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="KrishiMitra AI",
    page_icon="🌾",
    layout="wide"
)

# Application title
st.title("🌾 KrishiMitra AI")
st.subheader("Intelligent Crop Recommendations for Indian Farmers")

# Add month selector in main area
current_month = datetime.now().strftime("%B")
st.write("### 📅 Current Month:", current_month)

# Create three tabs for different features
tab1, tab2, tab3 = st.tabs(["Get Recommendations 🎯", "Crop Calendar 🗓️", "Farming Guidelines 📖"])

with tab2:
    st.header("Monthly Crop Calendar")
    
    crop_calendar = {
        "Kharif Crops (June-October)": {
            "Rice": "Jun-Jul",
            "Cotton": "May-Jun",
            "Maize": "Jun-Jul",
            "Sugarcane": "Feb-Mar",
            "Groundnut": "Jun-Jul"
        },
        "Rabi Crops (October-March)": {
            "Wheat": "Oct-Nov",
            "Mustard": "Oct-Nov",
            "Chickpea": "Oct-Nov",
            "Potato": "Oct-Nov",
            "Peas": "Oct-Nov"
        },
        "Zaid Crops (March-June)": {
            "Watermelon": "Feb-Mar",
            "Muskmelon": "Feb-Mar",
            "Cucumber": "Feb-Mar",
            "Vegetables": "Year-round"
        }
    }
    
    for season, crops in crop_calendar.items():
        st.subheader(season)
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Crop")
        with col2:
            st.write("Sowing Time")
            
        for crop, sowing_time in crops.items():
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"🌱 {crop}")
            with col2:
                st.write(sowing_time)

with tab3:
    st.header("General Farming Guidelines")
    
    with st.expander("🌡️ Weather Considerations"):
        st.write("""
        - Monitor local weather forecasts regularly
        - Plan irrigation based on rainfall predictions
        - Protect crops from extreme weather conditions
        - Consider crop insurance for weather-related risks
        """)
        
    with st.expander("💧 Water Management"):
        st.write("""
        - Implement water conservation techniques
        - Use drip irrigation when possible
        - Maintain proper drainage
        - Monitor soil moisture regularly
        """)
        
    with st.expander("🌿 Soil Health"):
        st.write("""
        - Get soil tested before each season
        - Follow recommended fertilizer dosage
        - Practice crop rotation
        - Use organic matter when possible
        """)
        
    with st.expander("💰 Financial Planning"):
        st.write("""
        - Calculate input costs before planting
        - Keep records of all expenses
        - Check current market prices
        - Consider government schemes and subsidies
        """)

# Sidebar for user inputs
st.sidebar.header("Enter Your Details")

# User inputs
pincode = st.sidebar.text_input("PIN Code", placeholder="Enter 6-digit PIN code")
land_area = st.sidebar.number_input("Land Area (acres)", min_value=0.1, max_value=1000.0, value=1.0)
budget = st.sidebar.number_input("Budget (₹)", min_value=1000, max_value=10000000, value=50000)

# Submit button
if st.sidebar.button("Get Recommendations"):
    if pincode and land_area and budget:
        try:
            # Preprocess user inputs
            processed_input = preprocess_user_input(pincode, land_area, budget)
            
            # Get recommendations
            recommendations = get_crop_recommendations(processed_input)
            
            with tab1:
                st.header("📊 Recommended Crops")
                
                for idx, crop in enumerate(recommendations, 1):
                    with st.expander(f"{idx}. {crop['name']} 🌱"):
                        # Basic Information
                        st.subheader("💰 Financial Overview")
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Expected ROI", f"₹{crop['roi']:,.2f}")
                            st.metric("Profit Potential", f"₹{crop['roi'] - crop['investment']:,.2f}")
                        
                        with col2:
                            st.metric("Investment Required", f"₹{crop['investment']:,.2f}")
                            st.metric("Per Acre Cost", f"₹{crop['investment']/land_area:,.2f}")
                            
                        with col3:
                            st.metric("Market Price Trend", "⬆️ Rising" if crop.get('price_trend', 0) > 0 else "⬇️ Falling")
                            st.metric("Market Demand", "High" if crop.get('demand', 'High') == 'High' else "Medium")
                        
                        # Crop Timeline
                        st.subheader("🗓️ Crop Timeline")
                        timeline_col1, timeline_col2 = st.columns(2)
                        
                        with timeline_col1:
                            st.metric("Time to Harvest", f"{crop['harvest_time']} months")
                            st.metric("Resilience Score", f"{crop['resilience']}/10")
                            
                        with timeline_col2:
                            st.subheader("📅 Best Sowing Window")
                            st.info(crop['sowing_window'])
                            
                            if 'critical_months' in crop:
                                st.warning(f"⚠️ Critical Care Months: {crop['critical_months']}")
                        
                        # Weather Information
                        st.subheader("🌤️ Weather Forecast & Impact")
                        weather_col1, weather_col2 = st.columns(2)
                        
                        with weather_col1:
                            st.line_chart(crop['weather_forecast'])
                            
                        with weather_col2:
                            st.write("Weather Impact Analysis:")
                            weather_impact = crop.get('weather_impact', {})
                            for factor, impact in weather_impact.items():
                                st.write(f"- {factor}: {impact}")
                        
                        # Detailed Guidelines
                        st.subheader("🌱 Cultivation Guidelines")
                        
                        with st.expander("Land Preparation"):
                            st.write(crop.get('land_preparation', [
                                "Ensure proper soil tillage",
                                "Remove weeds and crop residue",
                                "Level the field properly",
                                "Add organic matter if needed"
                            ]))
                            
                        with st.expander("Water Requirements"):
                            st.write(crop.get('water_requirements', [
                                "Regular irrigation needed",
                                "Maintain proper drainage",
                                "Monitor soil moisture"
                            ]))
                            
                        with st.expander("Fertilizer Schedule"):
                            st.write(crop.get('fertilizer_schedule', [
                                "Base fertilizer before sowing",
                                "Top dressing after 30 days",
                                "Micronutrient application if needed"
                            ]))
                        
                        # Additional Tips
                        st.subheader("💡 Key Success Factors")
                        tips_col1, tips_col2 = st.columns(2)
                        
                        with tips_col1:
                            st.write("Do's:")
                            for tip in crop['tips']:
                                st.markdown(f"✅ {tip}")
                                
                        with tips_col2:
                            st.write("Don'ts:")
                            for warning in crop.get('warnings', [
                                "Avoid over-irrigation",
                                "Don't ignore pest monitoring",
                                "Don't skip soil testing"
                            ]):
                                st.markdown(f"❌ {warning}")
                                
                        # Local Resources
                        st.subheader("🏢 Local Support")
                        if 'local_resources' in crop:
                            for resource in crop['local_resources']:
                                st.write(f"- {resource}")
                        else:
                            st.write("- Contact local Krishi Vigyan Kendra (KVK) for support")
                            st.write("- Join local farmer producer organizations")
                            st.write("- Connect with agricultural extension officers")
                        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please fill in all the required fields.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with ❤️ for Indian Farmers</p>
        <p>Data sources: Soil Health Card, AgMarkNet, ICRISAT/FAO</p>
    </div>
    """,
    unsafe_allow_html=True
)
