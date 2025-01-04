import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('cleaned_workforce_jobs.csv')
data.columns = ['Date', 'UK_Male', 'UK_Female', 'London_Male', 'London_Female']

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%b-%Y')

# Extract the year and add as a new column
data['Year'] = data['Date'].dt.year

# Group by year and calculate the mean employment numbers for each year
yearly_data = data.groupby('Year')[['London_Male', 'London_Female']].mean().reset_index()

# Calculate the total employment and year-over-year percentage changes
yearly_data['London_Total'] = yearly_data['London_Male'] + yearly_data['London_Female']
yearly_data['London_Male_Pct_Change'] = yearly_data['London_Male'].pct_change() * 100
yearly_data['London_Female_Pct_Change'] = yearly_data['London_Female'].pct_change() * 100
yearly_data['London_Total_Pct_Change'] = yearly_data['London_Total'].pct_change() * 100

# Remove the first row since it will have NaN changes
yearly_changes = yearly_data.dropna()

# Plot the bar chart
plt.figure(figsize=(12, 7))
bar_width = 0.35
x = yearly_changes['Year']

# Bars for males and females
plt.bar(x - bar_width/2, yearly_changes['London_Male_Pct_Change'], width=bar_width, label='Male % Change')
plt.bar(x + bar_width/2, yearly_changes['London_Female_Pct_Change'], width=bar_width, label='Female % Change', color='pink')

# Line for total percentage change
plt.plot(x, yearly_changes['London_Total_Pct_Change'], label='Total % Change', color='red', marker='o', linewidth=2)

# Add chart details
plt.title('Yearly Percentage Change in London Employment by Gender', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Year-over-Year % Change', fontsize=14)
plt.xticks(x, rotation=45)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  
plt.legend(title="Legend", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.tight_layout()

# Display the chart
plt.show()
