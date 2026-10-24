
import os
import pandas as pd

from sklearn.ensemble import IsolationForest

folder = "/Users/rajaansari/Documents/Project 2"

orders = pd.read_csv(
    os.path.join(folder, "olist_orders_dataset.csv")
)

payments = pd.read_csv(
    os.path.join(folder, "olist_order_payments_dataset.csv")
)

# 1. Delivered orders
orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"], errors="coerce"
)

delivered = orders[orders["order_status"] == "delivered"]

# 2. Match orders and payments
data = delivered.merge(payments, on="order_id", how="left")
data["payment_value"] = data["payment_value"].fillna(0)

data["month"] = data["order_purchase_timestamp"].dt.to_period("M").astype(str)

# 3. Monthly finance report
monthly = data.groupby("month").agg(
    Delivered_Orders=("order_id", "nunique"),
    Total_Payments=("payment_value", "sum")
).reset_index()

monthly["Growth_Percent"] = (
    monthly["Total_Payments"].pct_change() * 100
).round(2)

# 4. Payment method analysis
payment_methods = data.groupby("payment_type").agg(
    Transactions=("order_id", "count"),
    Total_Payments=("payment_value", "sum")
).reset_index()

# 5. Anomaly detection
valid = data[data["payment_value"] > 0].copy()

if len(valid) > 1:
    model = IsolationForest(
        contamination=0.01,
        random_state=42
    )
    valid["Anomaly"] = model.fit_predict(
        valid[["payment_value"]]
    )
    anomalies = valid[valid["Anomaly"] == -1]
else:
    anomalies = valid.copy()

# 6. Automatic business insights
insights = []

total_payments = data["payment_value"].sum()
total_orders = data["order_id"].nunique()

insights.append(f"Delivered orders analyzed: {total_orders}")
insights.append(f"Total payment value: {total_payments:,.2f}")

if not monthly.empty:
    best_month = monthly.loc[
        monthly["Total_Payments"].idxmax(), "month"
    ]
    insights.append(f"Highest payment month: {best_month}")

if not payment_methods.empty:
    best_method = payment_methods.loc[
        payment_methods["Total_Payments"].idxmax(),
        "payment_type"
    ]
    insights.append(f"Top payment method by value: {best_method}")

insights.append(
    f"Unusual payment records flagged for review: {len(anomalies)}"
)

# 7. Export all reports to Excel
output = os.path.join(folder, "Advanced_Finance_Report.xlsx")

with pd.ExcelWriter(output, engine="openpyxl") as writer:
    monthly.to_excel(writer, sheet_name="Monthly Summary", index=False)
    payment_methods.to_excel(writer, sheet_name="Payment Methods", index=False)
    anomalies.to_excel(writer, sheet_name="Anomalies", index=False)
    pd.DataFrame({"Business Insights": insights}).to_excel(
        writer, sheet_name="AI Insights", index=False
    )

print("\n--- MONTHLY SUMMARY ---")
print(monthly.tail())

print("\n--- PAYMENT METHODS ---")
print(payment_methods)

print("\n--- BUSINESS INSIGHTS ---")
for item in insights:
    print("-", item)

print("\nReport saved:", output)
