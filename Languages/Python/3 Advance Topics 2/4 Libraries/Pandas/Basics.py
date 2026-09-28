# Importing pandas library
import pandas as pd

import os

def change_dir() -> None:
    os.chdir("/storage/emulated/0/Programing/Python/2 Advance Topics 1/5 Libraries/Pandas/") 
    return

change_dir()
# --- Creating Series and DataFrame ---
# Create a Pandas Series
data = [10, 20, 30, 40]
series = pd.Series(data)
print("Pandas Series:")
print(series)

# Create a Pandas DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# --- Reading and Writing Data ---
# Reading data from a CSV file (if data.csv exists)
# df = pd.read_csv('data.csv')
# print("\nData from CSV:")
# print(df)

# Writing DataFrame to a CSV file
df.to_csv('output.csv', index=False)

# --- Indexing and Selecting Data ---
# Select a single column
age_column = df['Age']
print("\nSelected Age Column:")
print(age_column)

# Select multiple columns
subset = df[['Name', 'Age']]
print("\nSelected Subset (Name and Age):")
print(subset)

# Select rows by index using iloc
row = df.iloc[0]
print("\nFirst Row:")
print(row)

# Select multiple rows (first 2 rows)
rows = df.iloc[0:2]
print("\nFirst 2 Rows:")
print(rows)

# Conditional Selection - Select rows where age is greater than 30
over_30 = df[df['Age'] > 30]
print("\nRows where Age > 30:")
print(over_30)

# --- Handling Missing Data ---
# Detecting missing data (if any missing values exist in the DataFrame)
missing_data = df.isnull()
print("\nMissing Data (True indicates missing value):")
print(missing_data)

# Filling missing values with 0 (if any missing data exists)
df_filled = df.fillna(0)
print("\nDataFrame with Missing Values Filled:")
print(df_filled)

# --- Grouping and Aggregating Data ---
# Grouping data by 'City' and calculating the average 'Age' per city
grouped = df.groupby('City')['Age'].mean()
print("\nAverage Age per City:")
print(grouped)