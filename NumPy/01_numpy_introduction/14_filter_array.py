import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)  # [41 43]


print()
# Create a filter array that will return only values higher than 42:
arr2 = np.array([41, 42, 43, 44])
filter_arr = []
for element in arr2:
    # if the element is higher than 42, set the value to True, otherwise False:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr2 = arr[filter_arr]
print(filter_arr)  # [False, False, True, True]
print(newarr2)  # [43 44]


print()
# Create a filter array that will return only even elements from the original array:
arr3 = np.array([1, 2, 3, 4, 5, 6, 7])
# Create an empty list
filter_arr3 = []
for element in arr3:
    if element % 2 == 0:
        filter_arr3.append(True)
    else:
        filter_arr3.append(False)
newarr3 = arr3[filter_arr3]
print(filter_arr3)  # [False, True, False, True, False, True, False]
print(newarr3)  # [2 4 6]


print()
# Creating Filter Directly From Array
arr4 = np.array([41, 42, 43, 44])
filter_arr4 = arr > 42
newarr4 = arr4[filter_arr4]
print(filter_arr4)  # [False False  True  True]
print(newarr4)  # [43 44]


print()
# Create a filter array that will return only even elements from the original array:
arr5 = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr5 = arr5 % 2 == 0
newarr5 = arr5[filter_arr5]
print(filter_arr5)  # [False  True False  True False  True False]
print(newarr5)  # [2 4 6]
