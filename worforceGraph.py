import pandas as pd
import matplotlib.pyplot as plt 

def readWorforceCSV():
    data = pd.read_csv('workforce-jobs-ons.csv')
    data.columns = ['Date', 'UK_Male', 'UK_Female', 'London_Male', 'London_Female']
    data = data[1:].reset_index(drop=True)

    return data

worforceData = readWorforceCSV()

worforceData['Date'] = pd.to_datetime(worforceData['Date'])
"""
selected_years = [2019, 2020, 2022, 2023]
filtered_data = data[data['Date'].dt.year.isin(selected_years)].copy()

# Calculate percentage change by gender for London
filtered_data['London_Male_Percentage_Change'] = filtered_data['London_Male'].pct_change() * 100
filtered_data['London_Female_Percentage_Change'] = filtered_data['London_Female'].pct_change() * 100

#Create a line graph for percentage change in London employment by gender
plt.figure(figsize=(10, 6))
plt.plot(filtered_data['Date'], filtered_data['London_Male_Percentage_Change'], label='London Male', marker='o')
plt.plot(filtered_data['Date'], filtered_data['London_Female_Percentage_Change'], label='London Female', marker='o')
plt.title('Percentage Change in London Employment by Gender (2019-2023)')
plt.ylabel('Percentage Change (%)')
plt.xlabel('Year')
plt.legend(loc='upper left')
plt.grid(visible=True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show() """

