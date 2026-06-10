import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# LOAD DATA
# -----------------------------

income = pd.read_csv("FS_sp500_income.csv")
cashflow = pd.read_csv("FS_sp500_flow.csv")

# -----------------------------
# SELECT APPLE
# -----------------------------

Ticker = "AAPL"

income = income[income['Ticker'] == Ticker]
cashflow = cashflow[cashflow['Ticker'] == Ticker]

# -----------------------------
# EXTRACT REVENUE
# -----------------------------

revenue = income[income['Breakdown'] == 'totalRevenue']

current_revenue = float(revenue['recent'].values[0])
past_revenue = float(revenue['before_1'].values[0])

# -----------------------------
# EXTRACT FREE CASH FLOW
# -----------------------------

fcf = cashflow[cashflow['Breakdown'] == 'freeCashFlow']

current_fcf = float(fcf['recent'].values[0])

# -----------------------------
# CALCULATE REVENUE GROWTH
# -----------------------------

growth_rate = (current_revenue - past_revenue) / past_revenue

print("Revenue Growth Rate:", growth_rate)

# -----------------------------
# DCF MODEL PARAMETERS
# -----------------------------

projection_years = 5
discount_rate = 0.10
terminal_growth = 0.03

# -----------------------------
# PROJECT FUTURE CASH FLOWS
# -----------------------------

cash_flows = []

fcf_projection = current_fcf

for year in range(1, projection_years + 1):

    fcf_projection = fcf_projection * (1 + growth_rate)

    cash_flows.append(fcf_projection)

print("\nProjected Cash Flows:")
print(cash_flows)

# -----------------------------
# DISCOUNT CASH FLOWS
# -----------------------------

discounted_cf = []

for i, cf in enumerate(cash_flows):

    pv = cf / (1 + discount_rate) ** (i + 1)

    discounted_cf.append(pv)

# -----------------------------
# TERMINAL VALUE
# -----------------------------

terminal_value = (
    cash_flows[-1] * (1 + terminal_growth)
) / (discount_rate - terminal_growth)

terminal_pv = terminal_value / (1 + discount_rate) ** projection_years

# -----------------------------
# ENTERPRISE VALUE
# -----------------------------

enterprise_value = sum(discounted_cf) + terminal_pv

print("\nEnterprise Value Estimate:")
print(enterprise_value)

# -----------------------------
# VISUALIZATION 1
# PROJECTED CASH FLOWS
# -----------------------------

years = list(range(1, projection_years + 1))

plt.figure()

plt.plot(years, cash_flows, marker='o')

plt.title("Projected Free Cash Flow (DCF Model)")
plt.xlabel("Year")
plt.ylabel("Free Cash Flow")

plt.show()

# -----------------------------
# VISUALIZATION 2
# DISCOUNTED CASH FLOWS
# -----------------------------

plt.figure()

plt.bar(years, discounted_cf)

plt.title("Present Value of Future Cash Flows")
plt.xlabel("Year")
plt.ylabel("Discounted Cash Flow")

plt.show()

# -----------------------------
# VISUALIZATION 3
# VALUE BREAKDOWN
# -----------------------------

plt.figure()

components = ['Discounted Cash Flows', 'Terminal Value']
values = [sum(discounted_cf), terminal_pv]

plt.bar(components, values)

plt.title("Enterprise Value Composition")

plt.show()




      #GEMINI CODE
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. LOAD DATA
# -----------------------------
# We load without assuming headers are perfect
income = pd.read_csv("FS_sp500_income.csv")
cashflow = pd.read_csv("FS_sp500_flow.csv")

# -----------------------------
# 2. EXTRACT REVENUE (Income Dataset)
# -----------------------------
# We look in the VERY FIRST COLUMN (index 0) for the AAPL revenue row
# In your data, the row is literally 'AAPLtotalRevenue'
rev_row = income[income.iloc[:, 0].str.contains('AAPLtotalRevenue', na=False)]

if rev_row.empty:
    print("Could not find AAPL Revenue. Printing columns to help you:")
    print(income.columns.tolist())
else:
    # We take the 2nd column (index 1) for 'Recent' and 3rd (index 2) for 'Before_1'
    current_revenue = float(rev_row.iloc[0, 1]) 
    past_revenue = float(rev_row.iloc[0, 2])
    
    growth_rate = (current_revenue - past_revenue) / past_revenue
    print(f"Revenue Growth Rate: {growth_rate:.2%}")

# -----------------------------
# 3. EXTRACT FREE CASH FLOW (Cashflow Dataset)
# -----------------------------
# FCF = Cash from Ops (Index 1) + CapEx (Index 1)
# Looking for 'AAPLtotalCashFromOperatingActivities' and 'AAPLcapitalExpenditures'
ops_row = cashflow[cashflow.iloc[:, 0].str.contains('AAPLtotalCashFromOperatingActivities', na=False)]
cap_row = cashflow[cashflow.iloc[:, 0].str.contains('AAPLcapitalExpenditures', na=False)]

current_fcf = float(ops_row.iloc[0, 1]) + float(cap_row.iloc[0, 1])
print(f"Current Free Cash Flow: {current_fcf:,.2f}")

# -----------------------------
# 4. DCF MODEL
# -----------------------------
projection_years = 5
discount_rate = 0.10
terminal_growth = 0.02

projected_fcf = []
discounted_fcf = []

for year in range(1, projection_years + 1):
    fcf = current_fcf * ((1 + growth_rate) ** year)
    projected_fcf.append(fcf)
    discounted_fcf.append(fcf / ((1 + discount_rate) ** year))

terminal_value = (projected_fcf[-1] * (1 + terminal_growth)) / (discount_rate - terminal_growth)
terminal_pv = terminal_value / ((1 + discount_rate) ** projection_years)

enterprise_value = sum(discounted_fcf) + terminal_pv

print(f"\nEstimated Enterprise Value: ${enterprise_value:,.2f}")

# -----------------------------
# 5. QUICK PLOT
# -----------------------------
plt.bar(['Cash Flows', 'Terminal Value'], [sum(discounted_fcf), terminal_pv])
plt.title("AAPL Valuation Breakdown")
plt.show()
































