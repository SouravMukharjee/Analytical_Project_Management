import pandas as pd

# Load project data (Excel file)

try:
data = pd.read_excel("project_data.xlsx")
print("Project data loaded successfully.\n")
except FileNotFoundError:
print("project_data.xlsx not found. Please add the dataset.\n")
data = pd.DataFrame()

# Display basic overview

if not data.empty:
print("=== Project Data Overview ===")
print(data.head(), "\n")

```
# Example: Basic statistics for numeric columns
print("=== Summary Statistics ===")
print(data.describe(), "\n")

# Example: Estimation task simulation
if "Estimated_Hours" in data.columns and "Actual_Hours" in data.columns:
    data["Variance"] = data["Actual_Hours"] - data["Estimated_Hours"]
    print("=== Estimation Variance (Actual - Estimated) ===")
    print(data[["Estimated_Hours", "Actual_Hours", "Variance"]].head(), "\n")

# Example: Top 5 tasks by hours
if "Task" in data.columns and "Actual_Hours" in data.columns:
    top_tasks = data.sort_values("Actual_Hours", ascending=False).head(5)
    print("=== Top 5 Tasks by Actual Hours ===")
    print(top_tasks[["Task", "Actual_Hours"]], "\n")
```

else:
print("No data to analyze.\n")

print("Analytics in Project Management simulation complete.")

# I cannot share whole code for the University Group Security Pupose 
