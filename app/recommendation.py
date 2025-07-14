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
