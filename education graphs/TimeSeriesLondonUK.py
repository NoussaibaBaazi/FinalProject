import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/noussaibabaazi/Desktop/FinalProject/education graphs/Qualifications-of-working-age-NVQ.csv")

# Filter data for London and United Kingdom
london_uk_data = data[data['Area'].isin(['London', 'United Kingdom'])]

# Ensure the 'Year' column is numeric for sorting
london_uk_data['Year'] = pd.to_numeric(london_uk_data['Year'])

# Pivot data for plotting
pivot_data = london_uk_data.pivot(index='Year', columns='Area', values='% with NVQ4+ - aged 16-64: percent')

# Plot line graph
plt.figure(figsize=(10, 6))
for column in pivot_data.columns:
    plt.plot(pivot_data.index, pivot_data[column], marker='o', label=column)

plt.title('NVQ4+ Qualifications Over the Years: London vs United Kingdom', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage with NVQ4+', fontsize=12)
plt.legend(title='Region')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
