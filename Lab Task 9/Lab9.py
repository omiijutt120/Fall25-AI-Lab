import pandas as pd

# 1. LOAD THE DATASET
Dataset = pd.read_csv("ObesityDataSet.csv")

# 2. Print Top 5 rows of dataset: 
Dataset.head() 

#3. Print Bottom 5 rows of dataset: 
Dataset.tail() 

#4. Print Number of Rows and Columns in dataset: 
print('rows: ', Dataset.shape[0]) 
print('columns: ', Dataset.shape[1]) 

#5. Print/Determine all the null columns in dataset: 
Dataset.isnull().sum()

#6. Filling null values using mean / median / mode: 
Dataset = Dataset.fillna(Dataset.mean) 
Dataset = Dataset.fillna(Dataset.median) 
Dataset = Dataset.fillna(Dataset.mode) 

#7. Print datatype of each column: 
print(Dataset.dtypes)
