# AI-Powered Finance Reporting Automation

## Overview

A Python-based finance reporting project that analyzes e-commerce order
and payment data, generates Excel reports, highlights unusual payment
records, and supports visualization in Tableau.

## Features

-   Processes e-commerce order and payment datasets.
-   Generates Excel reports, including summary sheets.
-   Summarizes monthly payment trends and payment methods.
-   Flags unusual payment records using an anomaly-detection approach.
-   Presents results through Tableau dashboards.

## Tools & Technologies

-   Python
-   Pandas
-   Scikit-learn
-   Excel / XLSX
-   Tableau

## Dataset

The project uses Olist Brazilian e-commerce datasets, including
customer, order, payment, review, product, seller, and geolocation data.

## Files

-   `finance_automation.py` --- finance reporting workflow.
-   `Finance_Report.xlsx` --- generated finance report.
-   `Advanced_Finance_Report.xlsx` --- expanded report with additional
    analysis.
-   Tableau workbook files (`.twb`) --- dashboard definitions.
-   Olist CSV files --- source datasets.

## Example Findings

Results from the current run included: - Delivered orders: 96,478 -
Total payment value: 15,422,461.77 (dataset currency; confirm formatting
before presenting as a currency amount) - Highest-payment month:
November 2017 - Top payment method: credit card - 1,000 unusual payment
records flagged by the anomaly-detection workflow

An anomaly flag indicates a record worth reviewing; it does not prove
fraud.

## Setup

Create and activate a virtual environment if desired, then install the
packages used by the script:

``` bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install pandas openpyxl scikit-learn
```

## Run

``` bash
python3 finance_automation.py
```

The script should create the report files in the project directory. Open
the `.twb` workbook in Tableau Desktop and relink data sources if
Tableau requests them.

## Notes

-   Output values can change depending on the source data and code
    version.
-   "AI insights" in this project are rule-based summaries unless a
    generative AI model is explicitly integrated.
-   Verify the currency and units before using figures in a formal
    presentation.

## Author

Codewithme185
