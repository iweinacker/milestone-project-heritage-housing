import numpy as np
import streamlit as st
from src.data_management import load_house_price_data
from src.data_management import load_corr
from src.data_management import load_pkl_file

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")


def page_house_prices_study_body():

    # load housing data, correlation coefficients and a dictionary used in encoding
    # object variables
    df = load_house_price_data()
    df_corr = load_corr()
    dic = load_pkl_file('outputs/house_prices_study/v1/dic.pkl')

    # copied from HouseSalePrices study notebook
    
    st.write("### House Sale Price study")
    st.info(
        f"* The client is interested in discovering how the house attributes correlate with the sale price."
        f" Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.")
