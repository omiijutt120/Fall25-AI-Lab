import pandas as pd

fp = 'ObesityDataSet.csv'
dt = pd.read_csv(fp)

print('Dataset Loaded')

print('Top 5 Rows:')
print(dt.head())

print('\nBottom 5 Rows:')
print(dt.tail())

print('\nShape (Rows, Columns):', dt.shape)

print('\nNull Values Count:')
print(dt.isnull().sum())

print('\nColumn Data Types:')
print(dt.dtypes)
