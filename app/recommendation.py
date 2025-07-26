<<<<<<< HEAD
# app/recommendation.py

def recommend_crops(location, land_size, budget):
    """
    Dummy logic for now — replace with real ML model + rules later.
    """

    # Example: placeholder crops
    crops = [
        {"name": "Wheat", "roi": 25, "resilience": "High", "sowing_window": "Oct-Nov"},
        {"name": "Pulses", "roi": 30, "resilience": "Medium", "sowing_window": "Nov-Dec"},
        {"name": "Mustard", "roi": 20, "resilience": "High", "sowing_window": "Oct-Nov"}
    ]

    # Later: load your trained model, predict based on inputs.
    # This is just a fixed example.
    return crops[:3]
=======
import os
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_weather_data(pincode):
    """
    Fetch weather data from OpenWeatherMap API using PIN code
    """
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    
    # For demo, using dummy coordinates (will need to implement PIN to coord conversion)
    lat, lon = 28.6139, 77.2090  # Default to Delhi coordinates
    
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        raise Exception(f"Error fetching weather data: {str(e)}")

def calculate_resilience_score(crop, weather_data):
    """
    Calculate crop resilience score based on weather conditions
    """
    # Dummy implementation - to be replaced with actual ML model
    return np.random.randint(6, 10)

def calculate_roi(crop, investment, land_area):
    """
    Calculate expected Return on Investment
    """
    # Dummy implementation - to be replaced with actual calculations
    base_roi = {
        'rice': 1.4,
        'wheat': 1.3,
        'cotton': 1.6,
        'sugarcane': 1.5
    }
    return investment * (base_roi.get(crop, 1.4))

def get_sowing_window(crop, weather_data):
    """
    Determine the best sowing window based on weather forecast
    """
    # Dummy implementation - to be replaced with actual logic
    return "Best sowing time: Next 2-3 weeks"

def get_crop_recommendations(user_input):
    """
    Generate crop recommendations based on user input and environmental factors
    """
    weather_data = get_weather_data(user_input['pincode'])
    
    # Dummy crop data - to be replaced with ML model predictions
    recommended_crops = [
        {
            'name': 'Rice',
            'roi': calculate_roi('rice', user_input['budget'], user_input['land_area']),
            'resilience': calculate_resilience_score('rice', weather_data),
            'investment': user_input['budget'] * 0.8,
            'harvest_time': 4,
            'sowing_window': "Best time: June-July (Kharif) or Jan-Feb (Rabi)",
            'critical_months': "August-September (flowering stage)",
            'weather_forecast': pd.DataFrame(
                np.random.randn(7, 2),
                columns=['temperature', 'rainfall']
            ),
            'weather_impact': {
                "Temperature": "Optimal range: 20-35°C",
                "Rainfall": "Requires 100-200 cm during growing period",
                "Humidity": "High humidity beneficial during growth"
            },
            'price_trend': 1.2,
            'demand': 'High',
            'land_preparation': [
                "Plow the field 2-3 times",
                "Level the field for proper water distribution",
                "Create bunds for water retention",
                "Apply base fertilizer before transplanting"
            ],
            'water_requirements': [
                "Maintain 5cm water level during transplanting",
                "Increase to 10cm during tillering",
                "Drain field 10 days before harvest"
            ],
            'fertilizer_schedule': [
                "Base: NPK (20:20:20) during land preparation",
                "After 21 days: Top dress with Urea",
                "During panicle initiation: Apply potassium"
            ],
            'tips': [
                "Maintain proper water level in the field",
                "Monitor for pest infestations",
                "Apply fertilizer as per soil health card recommendations",
                "Use certified seeds for better yield"
            ],
            'warnings': [
                "Avoid over-flooding the field",
                "Don't skip regular monitoring for pests",
                "Don't harvest before proper maturity",
                "Avoid excessive nitrogen application"
            ],
            'local_resources': [
                "Rice Research Station - Contact: 1800-XXX-XXXX",
                "Local Seed Supplier: Agricultural Cooperative Society",
                "Nearest Processing Unit: District Rice Mill"
            ]
        },
        {
            'name': 'Cotton',
            'roi': calculate_roi('cotton', user_input['budget'], user_input['land_area']),
            'resilience': calculate_resilience_score('cotton', weather_data),
            'investment': user_input['budget'] * 0.7,
            'harvest_time': 6,
            'sowing_window': "Best time: April-May (Summer) or June-July (Kharif)",
            'critical_months': "August-September (flowering and boll formation)",
            'weather_forecast': pd.DataFrame(
                np.random.randn(7, 2),
                columns=['temperature', 'rainfall']
            ),
            'weather_impact': {
                "Temperature": "Optimal range: 25-35°C",
                "Rainfall": "Requires 60-100 cm during growing period",
                "Sunlight": "Needs full sun exposure"
            },
            'price_trend': 0.8,
            'demand': 'High',
            'land_preparation': [
                "Deep plowing recommended",
                "Create raised beds for better drainage",
                "Remove previous crop residue",
                "Apply organic matter before sowing"
            ],
            'water_requirements': [
                "Regular irrigation at 10-15 day intervals",
                "Critical irrigation during flowering",
                "Avoid waterlogging"
            ],
            'fertilizer_schedule': [
                "Base: NPK (15:15:15) during sowing",
                "After 30-40 days: Top dress with Urea",
                "Apply micronutrients if deficiency observed"
            ],
            'tips': [
                "Ensure proper spacing between plants",
                "Regular weeding is essential",
                "Monitor for bollworm infestation",
                "Practice integrated pest management"
            ],
            'warnings': [
                "Don't ignore early pest signs",
                "Avoid excessive nitrogen",
                "Don't delay picking of mature bolls",
                "Avoid irrigation during boll opening"
            ],
            'local_resources': [
                "Cotton Research Center - Contact: 1800-XXX-XXXX",
                "Pesticide Quality Testing Lab",
                "Cotton Farmers Producer Organization"
            ]
        }
    ]
    
    return recommended_crops
>>>>>>> b2cf3db (Initial commit: KrishiMitra AI application with comprehensive farmer interface)
