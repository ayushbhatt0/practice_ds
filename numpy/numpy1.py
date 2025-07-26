import numpy as np


# my1d=np.array([23,34,4,5,6,7,45,23])            # one dimensional array
# print(type(my1d))                       # checking its type/class



# my2d=np.array([[23,34,4,5],[6,7,45,23],[23,34,5,6],[56,43,7,2]])            # two dimensional array(4*4)
# print(type(my1d))
# print(my2d)






#                                 # creating an array


#             # using python list
# my_arr=np.array([[2,4,6,7],[23,4,7,3]])
# print(my_arr)

        #  or

# my=[23,45,6,3,43,2]
# arr=np.array(my)
# print(arr)
# print(type(arr))



#             # creating array with default values
#     # zero array
# zero_arr=np.zeros((3,4))
# print(zero_arr)

#     # ones array
# one_arr=np.ones((2,2))
# print(one_arr)

#     # defaut value
# default=np.full((2,3),6)        # syntex >>>  np.full((SHAPE),NUMBER)
# print(default)








#                         # array properties and operation

marks = np.array([56.5,45.7,67.6,64.4,58.9,54.2,48,39])

# print(marks.size)       #print size of array
# print(marks.shape)      # print shape of array
# print(marks.ndim)       # print dimentions of an array
# print(marks.dtype)      # print data type of elements of array


#         # changing data type of array  ( datatype conversion)
# change_arr= marks.astype(int)           # convert float into intezer array
# print(change_arr)




#                 # array operations

# print(marks+10)         # add 
# print(marks - 14)        # subtract
# print(marks * 2)        # multiply
# print(marks/3)          # devide 
# print(marks ** 3)       # power (marks with power of 3)
# print(marks % 2)        # modulas 




#                 # aggregation function

# sum = np.sum(marks)             # sum of all elements
# print(sum)

# print(np.mean(marks))           # avg of marks
# print(np.min(marks))            # minimum value of marks
# print(np.max(marks))            # maximum value of marks
# print(np.std(marks))            # standred diveation of marks

# variance= np.var(marks)         # variance of marks
# print(variance)








                                # indexing and slicing

one = np.array([11,12,23,43,53,6,532,23])
two = np.array([[12,23,34,45,56],[98,65,23,64,2]])

#         # indexing

# y = one[3]       # access 3rd index (4th element) of array 'one'
# r = two[1][3]       # access 1st index row and 3rd index column (1,3)
# print(y)
# print(r)



#         # fancy indexing

# y2= one[[2,4,5,6]]              # can access multiple indexes 
# print(y2)


#         # slicing 

# middle_part = one[2:8]                  # return a part of array  /,     syntex >> arr[strt:stop:step]
# print(middle_part)

# y=two[0:1]                      # slicing with 2dim array
# print(y)



#                 # boolean maskking  (access indexes based on conditions)

# big = two[two>40]               # access index value which are grater than 40
# print(big)



#                 # reshaping

# chng_one= one.reshape(2,2,2)            # changing one dimensional arary into 3 dim array 
# print(chng_one)
# print(chng_one.ndim)


# chng_two = two.flatten()                # changing multi_dim array into one_dim
# print(chng_two)                                 #(also can use .raval()  )










#                                 # updating or manuplating

        
#                 # adding a element   (.insert(array,index,value,axis=0/1))

#      # one dimensional
# one= np.insert(one,3,[35,23,43,32])
# print(one)

# # two dimensional
# two = np.insert(two,2,[23,45,46,474,8],axis=0)
# print(two)


#                 # concateanting arrays     (np.concatenate((arr_1, arr_2),axis))
# y= np.array([[1,2,3],[2,2,2]])
# x= np.array([[6,7,8],[3,3,3]])
# mew= np.concatenate((x,y),axis=1)
# print(mew)




#                 # removing elements             (np.delete(array,index,axis))
# print(two)
# new = np.delete(two,2,axis=1)
# print(new)




#                 # spliting array

# new1 = np.split(one,2)                  # equal parts
# print(new1)

# new2 = np.split(two,2)
# print(new2)

# new3= np.hsplit(two,5)
# print(new3)

# new4 = np.vsplit(two,2)
# print(new4)












prices=[100,200,300]
new=np.array(prices)
new2=new*(0.9)
print(new2)