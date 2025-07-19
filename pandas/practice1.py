import pandas as pd

data = pd.read_csv(r"C:\Users\acer\Downloads\people-1000.csv",encoding= 'utf-8')

# print(data.head(10))
# print(data.tail(10))

# print(data.info())

# print(data.describe())
# print(data['Phone'].describe())

# print(data.columns)

# print(data[['Phone','First Name']])

# print(data[(data['Index']>400) & (data['Sex']=='Male')])

