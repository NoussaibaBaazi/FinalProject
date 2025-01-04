import pandas as pd
import matplotlib.pyplot as plt

# Load your data
data = pd.read_csv("QualificationsCSV.csv")

# Filter for London data only
data_london = data[data["Area"] == "London"]

# Rename columns for clarity
columns_rename = {
    "% with NVQ4+: percent": "NVQ4+",
    "% with NVQ3 only: percent": "NVQ3 Only",
    "% with NVQ2 only: percent": "NVQ2 Only",
    "% with NVQ1 only - aged 16-64: percent": "NVQ1 Only",
    "% with Trade Apprenticeships : percent": "Trade Apprenticeships",
    "% with no qualifications: percent": "No Qualifications"
}

data_all_qualifications = data_london.rename(columns=columns_rename)[["Year"] + list(columns_rename.values())]

for col in columns_rename.values():
    data_all_qualifications[col] = pd.to_numeric(data_all_qualifications[col], errors='coerce')

data_all_qualifications["Year"] = data_all_qualifications["Year"].astype(int)

# Plotting
plt.figure(figsize=(12, 6))

for col, label in columns_rename.items():
    plt.plot(
        data_all_qualifications["Year"], 
        data_all_qualifications[label], 
        label=label, 
        linewidth=2
    )

plt.title("Qualification Levels in London by Year", fontsize=18)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Percentage", fontsize=14)
plt.xticks(data_all_qualifications["Year"], rotation=45)
plt.legend(title="Qualifications", fontsize=12, loc="center left")
plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.tight_layout() 
plt.ticklabel_format(style='plain', axis='y')

plt.show()
