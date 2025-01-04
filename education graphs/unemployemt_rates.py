import pandas as pd
import matplotlib.pyplot as plt

def read_unemployement_data():
    return pd.read_csv("annual-unemployment-region.csv")

data = read_unemployement_data()

london_data = data[data['Location'] == 'London']

years = london_data['Year']
unemployment_percent = london_data['percent']

plt.figure(figsize=(10, 6))
plt.plot(years, unemployment_percent, marker='o', label="Unemployment Rate")
plt.title("Unemployment Percentage in London (2004-2025)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Unemployment Percentage", fontsize=12)
plt.xticks(years, rotation=45)
plt.grid(visible=True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

