# pip install pandas

import pandas as pd

#Series:
# s = pd.Series([10, 20, 30, 40])
# print(s)

# s = pd.Series([10, 20, 30, 40], index=['a','b','c','d'])
# print(s)

# print(s['d'])

# print(s.mean())
# print(s.sum())
# print(s + 55)

#DataFrames:

# data = {
#     'Name': ["john","harry","Peter"],
#     'age': [19,20,18],
#     'Marks': [85,92,78],
#     'address': [266,511,80]
# }

# df = pd.DataFrame(data)

# print(df.head()) # first 5 rows

# print(df.tail(2)) # last 2 rows

# print(df.shape)

# print(df.columns)

# print(df['Name']) #Access a column

# print(df.iloc[2]) # Access by row index

# print(df.loc[0, 'Marks'])
# print(df.loc[1, 'Name'])

# Data Handling:

# df = pd.read_csv('data.csv')

# print(df.head())
# print(df.describe())
# print(df.info())

# fil = df[df['Age'] > 30]
# print(fil)

# fil = df[(df['Age'] > 30) & (df['Salary'] > 90000)]
# print(fil)

# df['Status'] = "Old"
# df.loc[df['Age'] < 30, 'Status'] = "Young"
# print(df.head())

# sort = df.sort_values(by='Age', ascending=False)
# print(sort)

# Handling Misiing values

# print(df.isnull())

# print(df.isnull().sum())

# df = pd.read_csv("data2.csv")

# print(df.dropna()) #remove rows with NaNs

# print(df.dropna(axis=1)) # remove columns with NaNs

# print(df.fillna(1)) #replace NaNs with 1

# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df['Salary'] = df['Salary'].fillna(df['Salary'].mean()) # fill with column mean

# print(df)
