import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 2)
print(newarr)  # [array([1, 2, 3]), array([4, 5, 6])]

print()
arr2 = np.array([1, 2, 3, 4, 5, 6])
newarr2 = np.array_split(arr2, 4)
print(newarr2)  # [array([1, 2]), array([3, 4]), array([5]), array([6])]

print()
arr3 = np.array([1, 2, 3, 4, 5, 6])
newarr3 = np.array_split(arr, 3)
print(newarr3[0])
print(newarr3[1])
print(newarr3[2])

print()
# Splitting 2-D Arrays
arr4 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr4 = np.array_split(arr4, 3)
print(newarr4)
"""
[array([[1, 2],
       [3, 4]]), 
   array([[5, 6],
       [7, 8]]), 
   array([[ 9, 10],
       [11, 12]])]
"""


print()
# Split the 2-D array into three 2-D arrays.
arr5 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18]]
                )
newarr5 = np.array_split(arr5, 3)
print(newarr5)
"""
[array([[1, 2, 3],
       [4, 5, 6]]),
 array([[ 7,  8,  9],
       [10, 11, 12]]),
 array([[13, 14, 15],
       [16, 17, 18]])]
"""

print()
# Uneven Split:
arr6 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [10, 11, 12],
                 [13, 14, 15],
                 [16, 17, 18],
                 [19, 20, 21]])

newarr6 = np.array_split(arr6, 3)
print(newarr6)
"""
[array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]), 
   array([[10, 11, 12],
       [13, 14, 15]]), 
   array([[16, 17, 18],
       [19, 20, 21]])]
"""


print()
# Split the 2-D array into three 2-D arrays along rows.
arr7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr7 = np.array_split(arr7, 3, axis=1)
print(newarr7)
"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), 
   array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), 
   array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""


print()
# The hsplit() method to split the 2-D array into three 2-D arrays along rows.
arr8 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr8 = np.hsplit(arr8, 3)
print(newarr8)
"""
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), 
   array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), 
   array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]
"""
