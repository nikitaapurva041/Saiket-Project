Customer Churn Prediction Project
📊 Project Overview
This project analyzes customer churn data to identify patterns and key factors influencing customer attrition. The analysis includes data cleaning, exploratory data analysis (EDA), and statistical insights to help businesses understand why customers leave and how to improve retention.

🎯 Objectives
Clean and preprocess raw customer data

Identify missing values and data type inconsistencies

Analyze customer churn patterns across different demographics and service attributes

Visualize key trends and relationships in the data

Provide actionable insights for customer retention strategies

📁 Project Structure
The project consists of several Jupyter notebooks, each focusing on a specific task:

Notebook	Description
Task 1.ipynb	Initial data loading, shape verification, and data type identification
Task 2.ipynb	Data cleaning - handling missing values, type conversion, duplicate removal, column standardization
Task 3.ipynb	Statistical analysis and exploratory data visualization
Task 4.ipynb	Customer segmentation by tenure and charge analysis
Task 5.ipynb	Advanced churn analysis by demographics, payment methods, contracts, and tenure groups
📈 Key Findings
Churn by Contract Type
Month-to-month contracts have the highest churn rate (~42.7%)

One-year contracts show significantly lower churn (~11.3%)

Two-year contracts have the lowest churn (~2.8%)

Churn by Payment Method
Electronic check users show highest churn (~45.3%)

Bank transfer and credit card users have much lower churn rates (~16-17%)

Churn by Tenure
0-12 months: ~47.7% churn (highest risk)

13-36 months: ~25.5% churn

37+ months: ~11.9% churn (lowest risk)

Churn by Senior Citizen Status
Senior citizens churn at ~41.7%

Non-senior citizens churn at ~23.6%

🛠️ Technologies Used
Python - Core programming language

Pandas - Data manipulation and analysis

NumPy - Numerical operations

Matplotlib - Static visualizations

Seaborn - Statistical data visualization

Plotly - Interactive visualizations

🔧 Data Processing Steps
Data Loading - Import CSV data from local directory

Missing Value Handling - Drop nulls and fill with appropriate values (mean for numerical, 0 for others)

Data Type Conversion - Convert TotalCharges to numeric, create categorical tenure_group column

Duplicate Removal - Remove duplicate records

Column Standardization - Convert column names to lowercase with underscores

Feature Engineering - Create tenure categories: 0-12, 13-36, 37+

📊 Visualizations Created
Histograms for MonthlyCharges distribution

Box plots for MonthlyCharges by Churn status

Box plots for Tenure by Churn status

Count plots for Churn distribution

Pie charts and donut charts for tenure group distribution

Bar charts for average charges by tenure group

💡 Recommendations
Based on the analysis:

Focus on retention efforts for customers in their first year

Incentivize longer-term contracts (one-year and two-year plans)

Review electronic check payment method - highest churn rate

Targeted programs for senior citizens who show higher churn

Early intervention for new customers (first 12 months)

🚀 How to Run
Ensure Python 3.x is installed

Install required packages:

bash
pip install pandas numpy matplotlib seaborn plotly
Update the file path in each notebook to point to your raw_data.csv location

Run the notebooks in order (Task 1 → Task 5)

📁 Data Source
The raw data file raw_data.csv contains customer information including:

Demographics (gender, senior citizen status, partner, dependents)

Account information (tenure, contract type, payment method, charges)

Services subscribed (phone, internet, security, backup, streaming)

Churn status (Yes/No)

📝 Notes
The dataset contains 7,043 customer records

Initial data cleaning revealed no missing values in most columns

TotalCharges required type conversion from string to numeric

Some TotalCharges values were empty strings and needed imputation

Analysis completed as part of a customer churn prediction project.

