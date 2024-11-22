import numpy as np

arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)  # 24
# 1*2*3*4 = 24


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x2 = np.prod([arr1, arr2])
print(x2)  # 40320
# 1*2*3*4*5*6*7*8 = 40320


arr3 = np.array([1, 2, 3, 4])
arr4 = np.array([5, 6, 7, 8])
newarr = np.prod([arr3, arr4], axis=1)
print(newarr)  # [  24 1680]

arr5 = np.array([1, 2, 3, 4])
newarr2 = np.cumprod(arr5)
print(newarr2)  # [ 1  2  6 24]
# [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

