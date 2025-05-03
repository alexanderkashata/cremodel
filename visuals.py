# visuals.py

import matplotlib.pyplot as plt
import streamlit as st

def plot_cashflow_chart(cash_flows):
    years = list(range(len(cash_flows)))
    plt.figure(figsize=(8, 4))
    plt.plot(years, cash_flows, marker='o')
    plt.title("Projected Annual Cash Flows")
    plt.xlabel("Year")
    plt.ylabel("Cash Flow ($)")
    st.pyplot(plt)
