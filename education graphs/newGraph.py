import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/noussaibabaazi/Desktop/FinalProject/education graphs/QualificatinsDataset.csv")

# Filter data for London only
london_data = data[data['Area'] == 'London']

# Extract relevant columns
years = london_data['Year']
nvq4_percent = london_data['% with NVQ4+ - aged 16-64: percent']
no_qualifications_percent = london_data['% with no qualifications - aged 16-64: percent']

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, nvq4_percent, marker='o', label='% with NVQ4+')
plt.plot(years, no_qualifications_percent, marker='o', label='% with No Qualifications')

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.title('Qualification Levels in London (NVQ4+ vs No Qualifications)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
