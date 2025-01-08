import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("QualificationsCSV.csv")

filtered_data = data[(data['Year'].isin([2013, 2021, 2020,2019])) & (data['Area'] == 'London')]
nvq4_data = filtered_data[['Year', 'Area', '% with NVQ4+: percent']]
print(nvq4_data)

numerical_columns = [
    '% with NVQ4+: percent',
    '% with NVQ3 only: percent',
    '% with NVQ2 only: percent',
    '% with NVQ1 only: percent',
    '% with no qualifications: percent'
]

summary_stats = data.groupby('Area')[numerical_columns].agg(['mean', 'median', 'min', 'max'])
print(summary_stats['% with NVQ4+: percent'])
print(summary_stats['% with no qualifications: percent'])
print(summary_stats['% with NVQ3 only: percent'])