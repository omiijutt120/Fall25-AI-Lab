import pandas as pd
import numpy as np

fp = 'ObesityDataSet.csv'
dt = pd.read_csv(fp)

# 1. Dealing with Null Values
num_c = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'SCC', 'SMOKE', 'CH2O', 'FAF', 'TUE']
cat_c = ['CALC']

for c in num_c:
    if c in dt.columns:
        dt[c] = dt[c].fillna(dt[c].median())

for c in cat_c:
    if c in dt.columns:
        dt[c] = dt[c].fillna(dt[c].mode()[0])

print('Null values after imputation:')
print(dt.isnull().sum())

# 2. Label Encoding (Converting Object columns to Int)
X = dt.drop('NObeyesdad', axis=1)
Y = dt['NObeyesdad']

obj_c = X.select_dtypes(['object']).columns

for c in obj_c:
    X[c], _ = pd.factorize(X[c])

Y_e, uc = pd.factorize(Y)
Y_e = pd.Series(Y_e)

print('\nDatatypes after Label Encoding:')
print(X.dtypes)
print('\nEncoded Target Classes:', uc.to_list())
