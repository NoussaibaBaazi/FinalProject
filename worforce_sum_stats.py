import pandas as pd

data = pd.read_csv("Data/cleaned_workforce_jobs.csv")
print(data.columns)
print(data.dtypes)

print(data.head())  
print(data.tail())  
summary_stats_all = data.drop(columns=['Date']).describe()

print(summary_stats_all.applymap("{:.2f}".format))