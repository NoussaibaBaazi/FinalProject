import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    """Reads a CSV file and returns a DataFrame."""
    return pd.read_csv("/Users/noussaibabaazi/Desktop/FinalProject/education graphs/Qualifications-of-working-age-NVQ_EDITED.csv")

data = read_data()
# Filter data for London only
london_data = data[data['Area'] == 'London']

# Extract relevant columns
years = london_data['Year']
nvq4_percent = london_data['% with NVQ4+ - aged 16-64: percent']
nvq2_percent = london_data['% with NVQ2 only - aged 16-64: percent']
nvq3_percent = london_data['% with NVQ3 only - aged 16-64: percent']
no_qualifications_percent = london_data['% with no qualifications - aged 16-64: percent']

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(years, nvq4_percent, label='% with NVQ4+')
plt.plot(years, no_qualifications_percent, label='% with No Qualifications')
plt.plot(years, nvq3_percent, label='% with NVQ3 only Qualifications')
plt.plot(years, nvq2_percent, label='% with NVQ2 only Qualifications')

# Add labels, title, and legend
plt.xlabel("Year", fontsize=12)
plt.xticks(years, rotation=45)
plt.ylabel('Percentage')
plt.title('Qualification Levels in London')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.grid(visible=True, linestyle='--', alpha=0.7)


# Show the plot
plt.show()
