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
    vars_to_study = ['OverallQual', 'GarageArea',
                     '2ndFlrSF', 'YearBuilt',]

    st.write("### House Sale Price study")
    st.info(
        f"* The client is interested in discovering how the house attributes correlate with the sale price."
        f" Therefore, the client expects data visualizations of the correlated variables against the sale price to show that.")


    # display housing data dataframe
    if st.checkbox("Inspect housing records dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")

        st.write(df.head(10))

    st.write("---")

    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to find  "
        f"the most important variables for determining the house sale price.  \n"
        f"The five most important variables are (in order of importance):  \n**{vars_to_study}**.  \n\n"
    )

    # Meaning of variables: From README file - "Dataset Content" section
    st.info(
        f"Meaning of variables:  \n"
        f"* **OverallQual**: Rates the overall material and finish of the house.  \n"
        f"* **GarageArea**: Above grade (ground) living area square feet. \n"
        f"* **2ndFlrSF**: Second floor square feet. \n"
        f"* **KitchenQual**: Kitchen quality. \n"
        f"* **YearBuilt**: Original construction date. \n"
    )


    st.image('Images/topvariable.png', caption='Top 5 Variables')



