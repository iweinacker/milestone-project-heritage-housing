import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load house price data


@st.cache_data()
def load_house_price_data():
    df = pd.read_csv(
        "outputs/datasets/collection/HousePricePredictionSales.csv")
    return df

# Load correlation coefficients (from HouseSalePrices notebook)


def load_corr():
    df = pd.read_csv("outputs/house_prices_study/v1/corr_df_rev.csv")
    return df

# Load pkl file


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)


# Example usage
if __name__ == "__main__":
    # Load your DataFrame or model here
    df = load_house_price_data()
    #print(df_example.head())  # Just for testing
