import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_house_prices_study import page_house_prices_study_body
from app_pages.page_predict_house_price import page_predict_house_price_body
from app_pages.page_ML_regressor_model import page_ML_regressor_model_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body

# Create an instance of the app
app = MultiPage(app_name="House Prices in Ames, Iowa")

# Add app pages using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("House Price Study", page_house_prices_study_body)
app.add_page("Predict House Price", page_predict_house_price_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Regressor Model", page_ML_regressor_model_body)

app.run()  # Run the app
