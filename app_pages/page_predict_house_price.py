import streamlit as st
import numpy as np
import pandas as pd
from src.data_management import load_house_price_data, load_pkl_file


def page_predict_house_price_body():
    # Load files needed for predicting house prices
    version = 'v1'
    pipeline = load_pkl_file(
        f"outputs/predict_price/{version}/best_regressor_pipeline.pkl")
    best_features = pd.read_csv(
        f"outputs/predict_price/{version}/X_train.csv").columns.to_list()

    # Load inherited houses file
    df = pd.read_csv(
        "inputs/datasets/raw/house-price-20211124T154130Z-001/house-price/inherited_houses.csv")


# Create input fields


def DrawInputsWidgets():

    # load dataset
    df = load_house_price_data()
    percentageMin, percentageMax = 0.5, 1.0

# we create input widgets only for three features
    col1, col2, col3 = st.columns(3)

    # We are using these features to feed the ML pipeline

    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

    # from here on we draw the widget based on the variable type (numerical or categorical)
    # and set initial values
    with col1:
        feature = "OverallQual"
        st_widget = st.selectbox(
            label=feature,
            options=df[feature].sort_values(ascending=True).unique()
        )
    X_live[feature] = st_widget

    with col2:
        feature = 'GrLivArea'
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    with co3:
        feature = 'GrLivArea'
        st_widget = st.number_input(
            label=feature,
            min_value=df[feature].min()*percentageMin,
            max_value=df[feature].max()*percentageMax,
            value=df[feature].median()
        )
    X_live[feature] = st_widget

    return X_live
