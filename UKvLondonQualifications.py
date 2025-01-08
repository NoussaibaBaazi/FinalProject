import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("QualificationsCSV.csv")

data_filtered = data[(data["Area"].isin(["London", "United Kingdom"])) & (data["Year"] == 2021)]

columns_rename = {
    "% with NVQ4+: percent": "NVQ4+",
    "% with NVQ3 only: percent": "NVQ3 Only",
    "% with NVQ2 only: percent": "NVQ2 Only",
    "% with NVQ1 only: percent": "NVQ1 Only",
    "% with Trade Apprenticeships: percent": "Trade Apprenticeships",
    "% with no qualifications: percent": "No Qualifications"
}

data_comparison = data_filtered.rename(columns=columns_rename)[["Area"] + list(columns_rename.values())]


data_comparison.set_index("Area", inplace=True)
data_comparison = data_comparison.T


data_comparison.plot(kind="bar", figsize=(12, 6), width=0.8)

plt.title("Qualification Levels in 2021: London vs UK", fontsize=18)
plt.xlabel("Qualification Levels", fontsize=14)
plt.ylabel("Percentage", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title="Area", fontsize=12, loc="upper right")
plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.tight_layout() 
plt.savefig('/Users/noussaibabaazi/Desktop/FinalProject/UKvLondonQualifications.png', dpi=300, bbox_inches='tight')

plt.show()
