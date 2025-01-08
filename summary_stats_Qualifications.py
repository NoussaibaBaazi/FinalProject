import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("QualificationsCSV.csv")

# Select relevant columns for analysis
numerical_columns = [
    '% with NVQ4+: percent',
    '% with NVQ3 only: percent',
    '% with NVQ1 only: percent',
    '% with no qualifications: percent'
]

summary_stats = data.groupby('Area')[numerical_columns].agg(['mean', 'median', 'min', 'max'])
print(summary_stats['% with NVQ4+: percent'])
print(summary_stats['% with no qualifications: percent'])