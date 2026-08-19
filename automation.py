import pandas as pd

# Load Data
df = pd.read_csv("data/sales_data.csv")   # Change filename if needed

print("Data Loaded Successfully")

# Clean Data
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

print("Data Cleaned Successfully")

# Save Processed Data
df.to_csv("data/processed_sales_data.csv", index=False)

print("Processed Data Saved")

# Basic Information
rows = len(df)
columns = len(df.columns)

summary = pd.DataFrame({
    "Metric": ["Total Rows", "Total Columns"],
    "Value": [rows, columns]
})

# Export to Excel
with pd.ExcelWriter("reports/Sales_Report.xlsx") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)

print("Excel Report Generated")
print("Pipeline Completed Successfully")