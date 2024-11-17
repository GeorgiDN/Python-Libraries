import numpy as np

# Reshape From 1-D to 2-D
# 4 arrays, each with 3 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)  # [ 1  2  3  4  5  6  7  8  9 10 11 12]
newarr = arr.reshape(4, 3)
print(newarr)
# output
"""
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
"""


print()
print()
# 2 arrays that contains 3 arrays, each with 2 elements
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr2 = arr2.reshape(2, 3, 2)
print(newarr2)
"""
[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]
"""


# Copy or View
print()
print()
arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr3.reshape(2, 4).base)


print()
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr4 = arr4.reshape(2, 2, -1)
print(newarr4)


print()
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
newarr5 = arr5.reshape(-1)
print(newarr5)  # [1 2 3 4 5 6]
