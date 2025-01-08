import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('cleaned_workforce_jobs.csv')
data.columns = ['Date', 'UK_Male', 'UK_Female', 'London_Male', 'London_Female']

#change date to a datatime format for analysis
data['Date'] = pd.to_datetime(data['Date'], format='%b-%Y')

#extract the year only
data['Year'] = data['Date'].dt.year

#Grouping all the quaretely data for each year
yearly_data = data.groupby('Year')[['London_Male', 'London_Female']].mean().reset_index()

#calculating the percentage change
yearly_data['London_Total'] = yearly_data['London_Male'] + yearly_data['London_Female']
yearly_data['London_Male_Pct_Change'] = yearly_data['London_Male'].pct_change() * 100
yearly_data['London_Female_Pct_Change'] = yearly_data['London_Female'].pct_change() * 100
yearly_data['London_Total_Pct_Change'] = yearly_data['London_Total'].pct_change() * 100

yearly_changes = yearly_data.dropna()


plt.figure(figsize=(12, 7))
bar_width = 0.35
x = yearly_changes['Year']

# Bars for males and females
plt.bar(x - bar_width/2, yearly_changes['London_Male_Pct_Change'], width=bar_width, label='Male % Change')
plt.bar(x + bar_width/2, yearly_changes['London_Female_Pct_Change'], width=bar_width, label='Female % Change', color='pink')

#line for total female and male percentage change
plt.plot(x, yearly_changes['London_Total_Pct_Change'], label='Total % Change', color='red', marker='o', linewidth=2)


plt.title('Yearly Percentage Change in London Employment by Gender', fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('% Change', fontsize=14)
plt.xticks(x, rotation=45)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  
plt.legend(title="Legend", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.tight_layout()
plt.savefig('/Users/noussaibabaazi/Desktop/FinalProject/WorkYearlyChange.png', dpi=300, bbox_inches='tight')
plt.show()

