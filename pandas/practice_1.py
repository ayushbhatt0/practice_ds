# data ==== supermarket sales data

                # TARGET  

# Perform data cleaning (e.g., check for missing values).

# Summarize total sales by branch or product line.

# Visualize quantity sold per product line.

# Group data by payment method or gender and calculate statistics.



import pandas as pd

data=pd.read_csv(r"C:\Users\acer\Documents\practice data\supermarket_sales.csv",encoding='utf-8')
print(data.head(),data.tail())           

print(data.info())              # checking some basic info about dataset

print(data.isnull().sum())          # checking fot missing values



                   # filling missing values

         # 1.. Invoice_ID
print(data['Invoice_ID'])    # to find , where is data missing
data.loc[8,'Invoice_ID']=109.           # filling missing value manually


          # 2.. Gender (filling manually acording to their names)
print(data[['Customer','Gender']])          # to check names and missing gender rows
data.loc[3,'Gender']='Male'
data.loc[6,'Gender']='Female'


         # 3.. Quantity (filling with estimate value)
data['Quantity']=data['Quantity'].interpolate(method='linear')





                        # summarise total sales 

        # summarise total sales by 'Branch'
data["total_sales"]=data['Quantity']*data['Unit_price']
print(data.groupby('Branch')['total_sales'].sum())

        # summarise total sales by 'Product_line'
print(data.groupby('Product_line')["total_sales"].sum())





