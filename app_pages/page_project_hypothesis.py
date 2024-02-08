import streamlit as st
from src.snsplot import plot_histogram_and_boxplot
from src.data_management import load_house_price_data


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from HouseSalePrices notebook
    st.success(
        f"* We suspect that the distribution of the sale prices is skewed to the right which might lead to a problem when it comes to predicting high sale prices."
        f" To validate the project hypothesis about the shape of the distribution, we plot a combined boxplot/histogram of the sale price."
        f"* As you can see in the next histogram and boxplots "

    )

    # plot combined boxplot/histogram of sale price - from HouseSalePrices notebook
    df2 = df.filter(['SalePrice'])
    plot_histogram_and_boxplot(df2)


st.info(
    f"* Hypothesis - Rates the overall material and finish of the house and Sale Price: "
    f" We realice that there is a significant positive relationship between the above-grade living area and the sale price. \n"
    f"* So our Null Hypotisis was rejected."

)
