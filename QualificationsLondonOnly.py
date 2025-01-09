import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("QualificationsCSV.csv")

#London data only needed for this analysis
data_london = data[data["Area"] == "London"]

#renaming columns for better clarity
columns_rename = {
    "% with NVQ4+: percent": "NVQ4+",
    "% with NVQ3 only: percent": "NVQ3 Only",
    "% with NVQ2 only: percent": "NVQ2 Only",
    "% with NVQ1 only: percent": "NVQ1 Only",
    "% with Trade Apprenticeships: percent": "Trade Apprenticeships percent",
    "% with no qualifications: percent": "No Qualifications"
}

data_all_qualifications = data_london.rename(columns=columns_rename)[["Year"] + list(columns_rename.values())]

#converting all values that must be numerical
for col in columns_rename.values():
    data_all_qualifications[col] = pd.to_numeric(data_all_qualifications[col], errors='coerce')


data_all_qualifications["Year"] = data_all_qualifications["Year"].astype(int)

#plotting figure
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
plt.savefig('/Users/noussaibabaazi/Desktop/FinalProject/LondonQualifications.png', dpi=300, bbox_inches='tight')

plt.show()

