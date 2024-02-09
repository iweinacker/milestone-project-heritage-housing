import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load house price data

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_price_data():
    df = pd.read_csv("outputs/datasets/collection/HousePricePredictionSales.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)
