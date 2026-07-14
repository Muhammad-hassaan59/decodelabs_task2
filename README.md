Data Analytics Project

🔹 Overview
This project explores a retail dataset using pandas and matplotlib inside an Anaconda virtual environment (task2).  
The goal is to clean the data, analyze numeric and categorical columns, and visualize distributions, correlations, and business insights.

---

🔹 Problem Statement
- Do some payment methods have more cancellations?  
- Which referral sources bring higher sales?  
- How do numeric columns like Quantity, UnitPrice, ItemsInCart, TotalPrice behave and relate to each other?

---

🔹 Methodology
1. Environment Setup  
   - Created virtual environment task2 in Anaconda.  
   - Installed pandas and matplotlib.  

2. Data Cleaning  
   - Checked null values (isna().sum()).  
   - Filled missing CouponCode with "Unknown".  
   - Capitalized string entries.  
   - Rounded TotalPrice to 2 decimals.  
   - Removed duplicates.  
   - Converted DateTime into Date.  

3. Analysis  
   - Descriptive statistics (describe(), five‑number summary).  
   - Checked skewness (mean vs median).  
   - Histograms and boxplots for distributions/outliers.  
   - Correlation matrix for numeric columns.  
   - Grouped summaries for categorical comparisons.  

4. Visualization  
   - Histograms for price distribution.  
   - Boxplots for spread and outliers.  
   - Bar charts for PaymentMethod vs OrderStatus.  
   - Bar charts for ReferralSource vs TotalPrice.

---

🔹 Key Findings
- PaymentMethod vs OrderStatus → Some methods (e.g., Debit Card, COD) show higher cancellation rates.  
- ReferralSource vs TotalPrice → Certain sources (e.g., Instagram, Direct Website) generate higher average sales.  
- Correlation analysis →  
  - ItemsInCart strongly correlates with TotalPrice.  
  - UnitPrice moderately correlates with TotalPrice.  
  - Quantity also correlates with TotalPrice.  
- Distribution analysis → Prices are slightly skewed, with outliers affecting averages.

---

🔹 Recommendations
- Focus marketing on referral sources that bring higher sales (e.g., Instagram).  
- Investigate payment methods with high cancellations (technical issues, customer trust).  
- Handle outliers carefully:  
  - Remove if noise (errors/typos).  
  - Investigate if signal (VIP customers, bulk orders).  
- Use correlation insights to design promotions that increase cart size → higher revenue.

---

🔹 How to Run
1. Clone this repository.  
2. Create and activate the Anaconda environment:  
   `bash
   conda create -n task2 python=3.10
   conda activate task2
   pip install pandas matplotlib
   `
3. Run the script:  
   `bash
   python analysis.py
   `
4. View outputs in terminal and plots in matplotlib windows
