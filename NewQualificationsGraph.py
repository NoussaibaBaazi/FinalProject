import pandas as pd
import matplotlib.pyplot as plt
#
# Load your data
data = pd.read_csv("QualificationsCSV.csv")

# Rename columns for clarity
columns_rename = {
    "% with NVQ4+ - aged 16-64": "NVQ4+",
    "% with NVQ3 only - aged 16-64": "NVQ3 Only",
    "% with NVQ2 only - aged 16-64": "NVQ2 Only",
    "% with NVQ1 only - aged 16-64": "NVQ1 Only",
    "% with no qualifications - aged 16-64": "No Qualifications"
}

# Extract and clean the data
data_all_qualifications = data.rename(columns=columns_rename)[["Year"] + list(columns_rename.values())].dropna()

# Convert percentages to numeric values
for col in columns_rename.values():
    data_all_qualifications[col] = pd.to_numeric(data_all_qualifications[col], errors='coerce')

# Convert Year to integer
data_all_qualifications["Year"] = data_all_qualifications["Year"].astype(int)

# Plot the line graph
plt.figure(figsize=(16, 8))

# Plot each qualification level as a separate line
for col, label in columns_rename.items():
    plt.plot(
        data_all_qualifications["Year"], 
        data_all_qualifications[label], 
        label=label, 
        linewidth=2.5
    )

# Add chart details
plt.title("Qualification Levels by Year", fontsize=18)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Estimated Count", fontsize=14)
plt.xticks(data_all_qualifications["Year"], rotation=45)
plt.legend(title="Qualifications", fontsize=12, loc="upper left")
plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.tight_layout()  # Ensure layout fits within the figure
plt.ticklabel_format(style='plain', axis='y')

# Display the chart
plt.show()
