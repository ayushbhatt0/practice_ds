import pandas as pd

        # reading a csv file 
data = pd.read_csv(r"C:\Users\acer\Documents\practice data\products-1000.csv",encoding = "UTF-8")


        # creating own data
dataf={'name':['ayush',None,'ram','shyam'],
       'age':[19,34,25,None],
       'course':['bca','h.m',None,'bsc'],
       'fees':[450,230,650,320]}

data2=pd.DataFrame(dataf)
# print(data2)

#         # display dataset
# print(data)


#         # save data
# data.to_json("file_name.json",index=False)



#         # get first and last N rows of dataset
# print(data.head(20))    # print first 20 rows
# print(data.tail(30))     # print last 30 rows  




#                 # to get overview of dataset
# print(data.info())



#                 # to get discriptive statistics of dataframe
# ds = data.describe()
# print(ds)



#                 # to check the columns of dataframe                         
# col =data.columns
# print(col)



#                # selecting a column
# # single col 
# name = data['Name']                                 
# print(name)

# # multiple columns
# pro = data[["Name","Availability"]]                            
# print(pro)




#                 # filtering rows by conditions
# # single condition
# print(data[data["Availability"] == "backorder"])

# # multiple conditions
# filter = data[(data['Availability']=='in_stock') & (data['Internal ID']>40)]
# print(filter)



#                         # modifing 

#                 # adding column
# #  by square bracket
# data2['village'] = ['pagari','up','maindkhal','kandi']
# print(data2)

# #  by INSERT  method
# data2.insert(1,'state',['uk','up','uk','uk'])
# print(data2)



#                 # removing colomn
# data2.drop(columns=["age",'course'],inplace=True)
# print(data2)


#                 # modifing the column
# # specific vlaue
# data2.loc[2,'course']='bba'
# print(data2)

# # whole column
# data2['fees']= data2['fees']*1.6
# print(data2)



#                         # handling missing values
#                 # finding missing values
# # 1>> isnull()      >> return bolean values
# print(data2.isnull())

# # 2 .>>  isnull().sum   >> retuen count of missing values in each column
# print(data2.isnull().sum())



#                 # removing null values
# data2.dropna(inplace=True)
# print(data2)


#                 # filling missing values
        # filling default values
data2['age'].fillna(data2['age'].mean(), inplace=True)
print(data2)

#         # filling estimate value
# data2['age']= data2['age'].interpolate(method='linear',implace=True)
# print(data2)


#                 # sorting column
#         # single column
# data2.sort_values(by="age",ascending=True,inplace=True)
# print(data2)



#                         # grouping 
#         # basic grouping
# grouped=data.groupby('Internal ID')['Name'].sum()
# print(grouped)




#                         # merging and joining
#         # merging two df
# coustomer=pd.read_csv(r"C:\Users\acer\Downloads\customers-1000.csv",encoding="UTF-8")
# people=pd.read_csv(r"C:\Users\acer\Downloads\people-1000.csv",encoding='UTF-8')

# # print(coustomer.head(),coustomer.tail())
# # print(people.head(),people.tail())

# common=pd.merge(coustomer,people,on='Date of birth',how='inner')
# print(common)