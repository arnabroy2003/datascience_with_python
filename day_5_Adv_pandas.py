import pandas as pd

# data = {
#     'Student': ['A','B','C','D','E'],
#     'Class': ['X','X','Y','Y','Y'],
#     'Marks': [58, 78, 92, 70, 88]
# }

# df = pd.DataFrame(data)

# grouped = df.groupby('Class')

# print(grouped['Marks'].mean())

# grouped = df.groupby('Class')
# print(grouped['Marks'].agg(['mean','max','min','sum']))

# student = pd.DataFrame({
#     'Roll': [1,2,3],
#     'Name': ['A','B','C']
# })

# marks = pd.DataFrame({
#     'Roll': [1,2,3],
#     'Marks': [90,85,73]
# })

# address = pd.DataFrame({
#     'Name': ['A','B','C'],
#     'Address': ['Mumbai','Delhi','Pune']
# })

# joined = pd.merge(student, marks, on='Roll', how='inner')

# result = pd.merge(joined, address, on='Name', how='inner')

# print(result)


# Group data.csv of employee by department and find the avarage salary