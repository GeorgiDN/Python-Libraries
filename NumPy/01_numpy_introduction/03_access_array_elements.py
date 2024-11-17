import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])  # 1

print()
print(arr[2] + arr[3])  # 7

print()
# Access 2-D Arrays
two_d_arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("Second element on 1st row: ", two_d_arr[0, 1])  # 2

print()
# Access 3-D Arrays
three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(three_d_arr[0, 1, 2])  # 6


print()
# Negative Indexing
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim: ', arr2[1, -1])
