# CREModel: Commercial Real Estate Investment Calculator 🏢📊

CREModel is a financial modeling tool built with Python and Streamlit to help analyze commercial real estate investments. It allows users to assess key financial metrics such as IRR, Cap Rate, and Cash-on-Cash Return based on property inputs, loan terms, and dynamic exit strategies.

## 🚀 Features

- **Interactive Streamlit App**: Clean UI for entering investment assumptions and visualizing results.
- **Exit Strategy Modeling**: Choose an exit year between 5–10 years to evaluate returns under various holding periods.
- **Amortization Support**: Annual loan amortization is incorporated to project debt service and principal paydown.
- **Financial Metrics Calculated**:
  - Internal Rate of Return (IRR)
  - Exit Cap Rate
  - Cash-on-Cash Return
  - Sale Proceeds & Net Equity
  - Debt Service and Loan Balance

## 📂 File Structure

cremodel/
│
├── app.py # Main Streamlit application
├── calculations.py # Backend logic for financial modeling
├── visuals.py # Chart rendering for Streamlit (in progress or optional)
├── readme.md # This file
└── requirements.txt # Required Python packages

bash
Copy
Edit

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cremodel.git
   cd cremodel
(Optional but recommended) Create a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
📈 Example Use Case
Enter the following:

Purchase Price: $12,000,000

NOI: $1,200,000

Exit Cap Rate: 6.5%

Loan Amount: $8,000,000

Interest Rate: 5.5%

Loan Term: 10 years

Exit Year: 7

And view your IRR, net proceeds, and loan balance updated live on-screen.

📌 Notes
Currently supports annual projections only.

Submarket comps feature planned for future versions.

Visual charting functionality is stubbed and can be extended in visuals.py.

🧑‍💻 Created By
Alex Kashata – University of Arkansas
Advanced Financial Modeling – Spring 2025
Instructor: [Insert Name if required]

yaml
Copy
Edit

---

Let me know if you want to include screenshots, a demo GIF, or a license section. Want me to tailor this for turning in on a learning portal like Blackboard too?







 
