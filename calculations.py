import numpy as np
import numpy_financial as npf

def calculate_metrics(purchase_price, income, expenses, loan, rate, term, exit_year, exit_cap_rate):
    r = rate / 100
    loan_payment = loan * r * (1 + r) ** term / ((1 + r) ** term - 1)

    cash_flows = [-1 * (purchase_price - loan)]
    noi_list = []
    remaining_loan_balance = loan

    for year in range(1, exit_year + 1):
        noi = income - expenses
        noi_list.append(noi)

        interest_payment = remaining_loan_balance * r
        principal_payment = loan_payment - interest_payment
        remaining_loan_balance -= principal_payment

        annual_cash_flow = noi - loan_payment

        if year == exit_year:
            sale_price = noi / (exit_cap_rate / 100)
            net_sale_proceeds = sale_price - remaining_loan_balance
            annual_cash_flow += net_sale_proceeds

        cash_flows.append(annual_cash_flow)

    irr = npf.irr(cash_flows) * 100

    return {
        "NOI": noi_list[0],
        "Cap Rate": (noi_list[0] / purchase_price) * 100,
        "Cash-on-Cash Return": (cash_flows[1] / (purchase_price - loan)) * 100,
        "IRR": irr,
        "cash_flows": cash_flows
    }
