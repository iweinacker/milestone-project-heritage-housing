import streamlit as st

# conclusions taken from HouseSalePrices notebook
st.success(
    f"* We suspect that there is a few very high sale prices."
    f" The combined boxplot/histogram below confirms that: The histogram extends far to the right."
    f" It has a long tail.  \n"
    f"* The price values well beyond the average range are called outliers and are shown as dots "
    f"to the right of the box in the boxplot. They correspond to sale prices"
    f" above $466075"

)
