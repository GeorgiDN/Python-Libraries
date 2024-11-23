import numpy as np

# Create Sets in NumPy
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)  # [1 2 3 4 5 6 7]


# Finding Union
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)  # [1 2 3 4 5 6]


# Finding Intersection
arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([3, 4, 5, 6])
newarr2 = np.intersect1d(arr3, arr4, assume_unique=True)
print(newarr2)  # [3 4]


# Finding Difference
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr3 = np.setdiff1d(set1, set2, assume_unique=True)
newarr4 = np.setdiff1d(set2, set1, assume_unique=True)
print(newarr3)  # [1 2]
print(newarr4)  # [5 6]


# Finding Symmetric Difference
set3 = np.array([1, 2, 3, 4])
set4 = np.array([3, 4, 5, 6])
newarr5 = np.setxor1d(set3, set4, assume_unique=True)
print(newarr5)  # [1 2 5 6]

