import pandas as pd
import matplotlib.pyplot as plt 

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('cleaned_workforce_jobs.csv')
data.columns = ['Date', 'UK_Male', 'UK_Female', 'London_Male', 'London_Female']
data = data[1:].reset_index(drop=True)

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Filter for selected years
selected_years = [2019, 2020, 2021, 2022, 2023]
filtered_data = data[data['Date'].dt.year.isin(selected_years)].copy()

# Extract year for plotting
filtered_data['Year'] = filtered_data['Date'].dt.year

# Plot the stacked bar chart
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['Year'], filtered_data['London_Male'], label='London Male')
plt.bar(filtered_data['Year'], filtered_data['London_Female'], bottom=filtered_data['London_Male'], label='London Female')

# Add titles and labels
plt.title('London Employment by Gender', fontsize=16)
plt.ylabel('Number of Employees (in thousands)', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.xticks(filtered_data['Year'], rotation=45)
plt.legend(loc='upper left', fontsize=10)

# Display the chart
plt.tight_layout()
plt.show()


