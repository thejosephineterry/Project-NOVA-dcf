\# 🚀 Project NOVA — M\&A DCF Valuation Model

\## Hypothetical Merger: Amazon (AMZN) + NVIDIA (NVDA)

\### Built by Opene-Terry Josephine | Data \& Financial Analyst



\---



\## The Thesis



In a world where AI infrastructure is the most valuable 

resource on earth, what happens when the cloud's largest 

operator merges with the AI chip market's dominant supplier?



Project NOVA models the financial reality of a hypothetical 

Amazon + NVIDIA merger — and answers the question every 

investor asks: \*\*what is this combined entity actually worth?\*\*



\---



\## Project Overview



| Item | Detail |

|---|---|

| Type | Hypothetical M\&A DCF Valuation |

| Companies | Amazon (AMZN) + NVIDIA (NVDA) |

| Data Source | S\&P 500 Financial Statements |

| Historical Period | FY2019 — FY2022 |

| Forecast Period | FY2023 — FY2027 |

| Tools Used | Python · Excel · Pandas · Matplotlib · Seaborn |



\---



\## Methodology



\### Step 1 — Historical Analysis

Extracted 4 years of real financial data for both companies

from S\&P 500 income statement and cash flow datasets.

Constructed a pro forma combined entity (NOVA) by merging

financials across all key metrics.



\### Step 2 — Assumptions Framework

Built a documented assumptions model covering:

\- Revenue growth rates (Year 1-5)

\- FCF margins (Year 1-5)

\- Merger synergy premiums (0% → 5% → 8%)

\- WACC derived from CAPM

\- Terminal growth rate anchored to GDP



\### Step 3 — DCF Projection

Projected 5 years of Free Cash Flow using compounding

revenue growth and expanding FCF margins. Discounted all

cash flows back to present value using WACC of 9.5%.



\### Step 4 — Valuation

Applied Gordon Growth Model for terminal value.

Calculated Enterprise Value and Equity Value.

Built sensitivity analysis across WACC and TGR ranges.



\---



\## Key Assumptions



| Assumption | Value | Rationale |

|---|---|---|

| WACC | 9.5% | CAPM — blended Amazon + NVIDIA |

| Terminal Growth Rate | 3.0% | Above GDP — AI sector justified |

| Year 1 Revenue Growth | 12% | AI boom + AWS expansion |

| Year 2 Revenue Growth | 14% | Synergy realisation |

| Peak FCF Margin | 10.5% | Operating leverage + CapEx normalisation |

| Synergy Premium | 8% (Year 3+) | Conservative M\&A synergy estimate |

| Net Debt | $32,000M | Combined entity net debt position |



\---



\## Key Results



| Metric | Value |

|---|---|

| \*\*Enterprise Value\*\* | \*\*$352,396M\*\* |

| \*\*Equity Value\*\* | \*\*$320,396M\*\* |

| Base Revenue (FY2022) | $117,915M |

| Year 5 Projected Revenue | $267,330M |

| 5Y Revenue Growth | 127% |

| Year 1 FCF | $11,226M |

| Year 5 FCF | $28,070M |

| FCF Transformation | -$7,138M → +$28,070M |



\---



\## Key Findings



NOVA's historical Free Cash Flow was deeply volatile — 

swinging from +$17.4B in FY2019 to -$7.1B in FY2022. 

This was driven by Amazon's aggressive capital investment 

in AWS infrastructure and logistics — not structural weakness.



As that investment phase concludes, the combined entity is 

positioned for significant FCF expansion. By Year 5, NOVA 

projects $28.1B in annual free cash flow — a transformation 

underpinned by AI infrastructure demand, cloud scalability, 

and merger synergies.



The sensitivity analysis reveals Enterprise Value ranging 

from $231B to $755B across WACC and terminal growth 

scenarios — with our base case of $352B sitting conservatively 

in the middle of that range.



\---



\## Visualisations



\### Executive Dashboard

!\[Dashboard](nova\_executive\_dashboard.png)



\### Revenue Journey

!\[Revenue](nova\_revenue\_story.png)



\### FCF Transformation

!\[FCF](nova\_fcf\_transformation.png)



\### Sensitivity Heatmap

!\[Sensitivity](nova\_sensitivity\_heatmap.png)



\---



\## Repository Structure 







\---



\## How To Run



```python

\# Clone the repository

git clone https://github.com/thejosephineterry/Project-NOVA-dcf.git



\# Navigate to folder

cd Project-NOVA-dcf



\# Install dependencies

pip install pandas numpy matplotlib seaborn jupyter



\# Launch notebook

jupyter notebook Project\_NOVA\_DCF\_Analysis.ipynb

```



\---



\## About The Analyst



\*\*Opene-Terry Josephine\*\* — Data \& Financial Analyst  

Specialising in quantitative financial modelling, credit risk 

analysis, and investment research.



📧 josephineopeneterry@gmail.com  

💼 github.com/thejosephineterry  

✅ Available for remote roles worldwide

