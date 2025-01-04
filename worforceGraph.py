import pandas as pd
import matplotlib.pyplot as plt 

# Load the data
data = pd.read_csv('cleaned_workforce_jobs.csv')
data.columns = ['Date', 'UK_Male', 'UK_Female', 'London_Male', 'London_Female']

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%b-%Y')

# Extract the year and add as a new column
data['Year'] = data['Date'].dt.year

# Aggregate data by year (average for each year)
aggregated_data = data.groupby('Year')[['London_Male', 'London_Female']].mean().reset_index()

# Plot the line chart
plt.figure(figsize=(12, 7))
plt.plot(
    aggregated_data['Year'], 
    aggregated_data['London_Male'], 
    label='London Male', 
    marker='o', 
    linewidth=2
)
plt.plot(
    aggregated_data['Year'], 
    aggregated_data['London_Female'], 
    label='London Female', 
    marker='o', 
    linewidth=2, color='pink'
)

# Add chart details
plt.title('London Employment by Gender', fontsize=18)
plt.ylabel('Number of Employees (in thousands)', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.xticks(aggregated_data['Year'], rotation=45)
plt.legend(title="Gender", loc='upper left', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for clarity
plt.tight_layout()

# Display the chart
plt.show()


