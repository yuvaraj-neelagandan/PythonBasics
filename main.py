# data types & variables

a = 1 # int
b = 1.5 # float/double
c = 'c' # char
d = False # bool
e = 1 + 2j # complex no
f = "this is a sentence" # string
g = [1,2,3,4,5] # array/list
h = (3,4,5) # tuple
j = {"key": 1, "value": "this is the data"} # dict

data = 1
data = 2
data = 3
# print(data)

# arrays / list
array_data = [1,1.5,True,[1,2,3]] # collection of similar or non-similar data objects
# print(array_data)

# variable declaration syntax

#1. Variable One - wrong
#2. VariableOne - right - python package name, class name
#3. varaible_one - variable declaration, func_name - prefered


similar_array = [1,2,3,4,5]

# for

# for i in range(10,20): # 0 - range-1
#     print("Hello World")

result = 0 # global variable
for data in similar_array:
    result = result + data
    # print(result)
    # print(data)

# print(result) # pre defined

# while

# print(similar_array)

# functions - 4 type

def sum_of_arrays(): # function definition
    result = 0 # local variable
    for data in similar_array:
        result = result + data
        print(result)


# sum_of_arrays() # function call

# 1. with arg - with return
# 2. without arg - with return
# 3. with arg - without return
# 4. without arg - without return
# HW
# while

def sum_of_nos(a,b):
    return a+b

def sub_of_nos(a,b):
    print(a-b)

import time

def get_time():
    return str(time.time())

print(get_time())









