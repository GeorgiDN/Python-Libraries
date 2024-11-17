import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # [2 3 4 5]


print()
arr2 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr2[4:])  # [5 6 7]


print()
arr3 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr3[:4])  # [1 2 3 4]


print()
# Negative Slicing
arr4 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr4[-3:-1])  # [5 6]


# STEP
print()
arr5 = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr5[1:5:2])  # [2 4]


print()
ar6 = np.array([1, 2, 3, 4, 5, 6, 7])
print(ar6[::2])  # [1 3 5 7]


print()
# Step two day array
arr7 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr7[1, 1:4])  # [7 8 9]


print()
arr8 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr8[0:2, 2])  # [3 8]


arr9 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr9[0:2, 1:4])  # [[2 3 4][7 8 9]]
