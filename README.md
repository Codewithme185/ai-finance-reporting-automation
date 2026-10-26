# AI-Powered Finance Reporting Automation

## Overview

**AI-Powered Finance Reporting Automation** is a Python-based data analytics project that automates financial reporting for e-commerce transactions. It processes order and payment data, generates Excel reports, identifies unusual payment records, and supports interactive financial analysis through Tableau dashboards.

The project demonstrates how Python, data analysis, and business intelligence tools can streamline reporting workflows and help identify patterns in financial data.

## Features

- **Automated Data Processing:** Processes e-commerce order and payment datasets using Python.
- **Excel Report Generation:** Creates structured financial reports with summary sheets and analytical insights.
- **Monthly Payment Analysis:** Identifies payment trends and changes over time.
- **Payment Method Analysis:** Summarizes transactions by payment method.
- **Anomaly Detection:** Flags unusual payment records for further investigation.
- **Tableau Dashboards:** Supports visual analysis of financial performance and transaction trends.
- **Reporting Automation:** Reduces repetitive manual data processing and reporting tasks.

## Tools & Technologies

- **Programming Language:** Python
- **Data Analysis:** Pandas
- **Machine Learning:** Scikit-learn
- **Excel Automation:** OpenPyXL
- **Data Visualization:** Tableau
- **Data Format:** CSV and XLSX

## Dataset

This project uses the **Olist Brazilian E-Commerce Public Dataset**, which contains information about e-commerce orders and transactions.

The datasets used in the analysis include:

- Customers
- Orders
- Order Payments
- Order Reviews
- Products
- Sellers
- Geolocation

These datasets enable analysis of order fulfillment, payment behavior, financial trends, and potentially unusual transactions.

## Project Structure

```text
AI-Powered-Finance-Reporting/
│
├── finance_automation.py
├── Finance_Report.xlsx
├── Advanced_Finance_Report.xlsx
├── *.twb
├── *.csv
└── README.md
```

*Note: The actual filenames and folder structure may vary depending on the files included in the repository.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Codewithme185/AI-Powered-Finance-Reporting.git
cd AI-Powered-Finance-Reporting
```

Replace the repository URL and directory name if your actual GitHub repository uses a different name.

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate the Environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows**

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
python3 -m pip install pandas openpyxl scikit-learn
```

## Run the Project

Execute the main Python script:

```bash
python3 finance_automation.py
```

The script processes the available source datasets and generates the configured Excel reports.

To explore the visualizations, open the Tableau workbook (`.twb`) in Tableau Desktop. Relink the data sources if necessary.

## Key Business Findings

The following results were observed in the current project run:

| Metric | Result |
|---|---:|
| Delivered Orders | 96,478 |
| Total Payment Value | 15,422,461.77 |
| Highest-Payment Month | November 2017 |
| Leading Payment Method | Credit Card |
| Unusual Records Flagged | 1,000 |

**Important:** The payment value is reported in the dataset's numerical units. Confirm the currency and aggregation method before presenting it as a financial amount.

Anomaly detection identifies records that may warrant further review. A flagged record does not necessarily indicate fraud or suspicious activity.

## Generated Outputs

### Excel Reports

- `Finance_Report.xlsx` — financial summaries and reporting outputs.
- `Advanced_Finance_Report.xlsx` — expanded financial analysis and additional reporting.

### Tableau Dashboards

The Tableau workbooks (`.twb`) contain dashboard definitions for visualizing financial trends and exploring transaction data. Data-source paths may need to be updated when opening the workbooks on another computer.

## Business Applications

This project demonstrates practical applications of data analytics in finance and e-commerce:

- Automating recurring financial reports.
- Monitoring monthly payment trends.
- Comparing payment methods.
- Identifying transactions that require further investigation.
- Supporting data-driven financial reporting and decision-making.
- Reducing manual spreadsheet preparation.

## Limitations

- Results depend on the source datasets and the implemented analysis logic.
- Anomaly detection is intended to identify unusual patterns, not confirm fraudulent transactions.
- Any generated insights are based on the implemented rules and statistical methods; generative AI is not implied unless explicitly integrated.
- Tableau workbook portability depends on the availability and configuration of the source data.

## Future Improvements

- Schedule automated report generation.
- Add interactive filters and KPI tracking.
- Integrate more advanced anomaly-detection techniques.
- Add automated data-quality checks and validation.
- Develop a web-based financial reporting interface.
- Expand reporting to include revenue, order value, payment status, and customer-level trends.

## Author

**Codewithme185**

GitHub: [@Codewithme185](https://github.com/Codewithme185)

---

*Built to demonstrate Python-based financial reporting automation, data analysis, anomaly detection, and business intelligence visualization.*
