# app/data_preprocessing.py

import pandas as pd

def clean_soil_data(filepath):
    df = pd.read_csv(filepath)
    # Example cleaning steps
    df = df.dropna()
    # Add more cleaning as needed
    return df

def merge_datasets(soil_df, yield_df):
    # Example merge
    merged_df = pd.merge(soil_df, yield_df, on="region_id")
    return merged_df
