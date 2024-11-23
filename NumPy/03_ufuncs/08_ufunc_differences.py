import numpy as np

arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)  # [  5  10 -20]

"""
1. 15-10=5
2. 25-15=15
3. 5-25=5
"""

arr2 = np.array([20, 30, 40, 50])
newarr2 = np.diff(arr2)
print(newarr2)  # [10 10 10]


arr3 = np.array([10, 15, 25, 5])
newarr3 = np.diff(arr3, n=3)
print(newarr3)  # [  5 -30]

"""
n1 [  5  10 -20]
n2 [  5 -30]
n3 [-35]
"""
