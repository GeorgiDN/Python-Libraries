import numpy as np

# Sort the array:
# returns a copy of the array, leaving the original array unchanged.
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))  # [0 1 2 3]
print(arr)  # [3 2 0 1]


print()
# Sort the array alphabetically:
arr2 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr2))  # ['apple' 'banana' 'cherry']


print()
# Sort a boolean array:
arr3 = np.array([True, False, True])
print(np.sort(arr3))  # [False  True  True]


print()
# Sorting a 2-D Array
arr4 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr4))
# [[2 3 4]
#  [0 1 5]]

