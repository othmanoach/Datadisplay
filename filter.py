import pandas as pd
import matplotlib.pyplot as plt

while True:
    try:
        file_name = str(input("Enter file name : "))
        df = pd.read_csv(file_name)

        break
    except FileNotFoundError:
        print("This file doesn't existe")


print(df.head())

# 1. How many rows are in the dataset?
rows = len(df)
print("\nNumber of Rows: ", rows)

# 2. What is the column names?
cols = df.columns
print("\nColumn Names: ", cols)

# 3. What is the data type for each columns?
data_types = df.dtypes
print("\nData Types: \n", data_types)
# 4. Which column has missing values?
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values[missing_values > 0])
