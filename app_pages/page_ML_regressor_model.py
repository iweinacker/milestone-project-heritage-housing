import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_pkl_file
from src.evaluate import regression_performance, regression_evaluation, regression_evaluation_plots


def page_ML_regressor_model_body():


    st.write("### ML house price pipeline")

    # summary of model performance
    st.info(
        f"* We agreed with the client on an R2 score of at least 0.75 on both train and test "
        f"set.  \n"
        f"* Our pipeline achieves 0.95 and 0.80 on the train set and test set respectively  \n"
    )
    st.write("---")

    # show pipeline steps
    st.write("* **ML pipeline to predict house sale price**")
    st.image('Images/pipeline.png', caption='Best Pipeline')
    st.write("---")

    # show best features and their importance for the ML model
    st.write("* **The features the model was trained on and their importance**")
    st.info("The most important variable for predicting the sale price is 'OverallQual'")
    st.image('Images/Importance-feature.png', caption='Importance Features')
    st.write("---")

    # evaluate performance on train and test sets
    st.image('Images/model-evaluation.png', caption='Model Evaluation')

    st.write("---")

    # Plot predicted versus actual sale price for train and test sets
    st.write("* **Predicted versus actual sale price scatterplot**")
    st.info("* For prices below $400,000, the data points closely align with the red line, indicating"
            " that our models predicted prices match the actual prices.  \n"
            "* However, for higher prices, our model tends to underestimate. In the scatterplot "
            "showing predictions on the train set (left plot), data points above $400,000 fall below"
            "the red line."
            )

    st.image('Images/trainandtest.png', caption='Sale price scatterplots')
