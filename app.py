# app.py

import streamlit as st
from calculations import calculate_metrics
from visuals import plot_cashflow_chart

# Page setup
st.set_page_config(page_title="CREModel", layout="centered")
st.title("🏢 CREModel: Real Estate Investment Calculator")

# Sidebar inputs
st.sidebar.header("📥 Investment Inputs")
purchase_price = st.sidebar.number_input("Purchase Price ($)", value=1_000_000)
rental_income = st.sidebar.number_input("Annual Rental Income ($)", value=120_000)
operating_expenses = st.sidebar.number_input("Annual Operating Expenses ($)", value=30_000)
loan_amount = st.sidebar.number_input("Loan Amount ($)", value=700_000)
interest_rate = st.sidebar.slider("Interest Rate (%)", 3.0, 10.0, 5.0)
loan_term = st.sidebar.number_input("Loan Term (Years)", value=25)
exit_year = st.sidebar.slider("Exit Year", 5, 10, 5)
exit_cap_rate = st.sidebar.number_input("Exit Cap Rate (%)", value=6.0)

# Calculate results
metrics = calculate_metrics(
    purchase_price, rental_income, operating_expenses,
    loan_amount, interest_rate, loan_term, exit_year, exit_cap_rate
)

# Display investment metrics
st.subheader("📊 Investment Metrics")

# Format and show only numeric keys
safe_keys = ["NOI", "Cap Rate", "Cash-on-Cash Return", "IRR"]

for key in safe_keys:
    value = metrics.get(key)
    if isinstance(value, (int, float)):
        if "Return" in key or "IRR" in key or "Cap Rate" in key:
            st.metric(label=key, value=f"{value:.2f}%")
        else:
            st.metric(label=key, value=f"${value:,.2f}")

# Cash flow chart
st.subheader("📈 Projected Annual Cash Flows")
plot_cashflow_chart(metrics["cash_flows"])
