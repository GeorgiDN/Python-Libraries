import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)  # (array([3, 5, 6]),)
print(x[0])  # [3 5 6]

print()
# Find the indexes where the values are even
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x2 = np.where(arr2 % 2 == 0)
print(x2)  # (array([1, 3, 5, 7]),)
print(x2[0])  # [1 3 5 7]


print()
# Find the indexes where the values are odd
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x3 = np.where(arr3 % 2 == 1)
print(x3)  # (array([0, 2, 4, 6]),)
print(x3[0])  # [0 2 4 6]


print()
# Find the indexes where the value 7 should be inserted:
arr4 = np.array([6, 7, 8, 9])
x4 = np.searchsorted(arr4, 7)
print(x4)  # 1


print()
# Find the indexes where the value 7 should be inserted, starting from the right:
arr5 = np.array([6, 7, 8, 9])
x5 = np.searchsorted(arr5, 7, side='right')
print(x5)  # 2


print()
# Find the indexes where the values 2, 4, and 6 should be inserted:
arr6 = np.array([1, 3, 5, 7])
x6 = np.searchsorted(arr6, [2, 4, 6])
print(x6)
