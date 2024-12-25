import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/noussaibabaazi/Desktop/FinalProject/education graphs/Qualifications-of-working-age-NVQ.csv")

london_data = data[data['Area'] == 'London']
other_regions_data = data[data['Area'] != 'London']

# Combine the data for comparison
comparison_data = pd.concat([london_data, other_regions_data])

# Plot bar chart for NVQ4+ percentages
plt.figure(figsize=(12, 6))
plt.bar(comparison_data['Area'], comparison_data['% with NVQ4+ - aged 16-64: percent'], color='skyblue')
plt.title('Comparison of NVQ4+ Qualifications: London vs Other Regions', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Percentage with NVQ4+', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
