import numpy as np

print(np.sum([1, 2, 3, 4]))  # 10

# 1+2+3+4
print(4*(4+1) / 2)  # 10

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
newarr = np.add(arr1, arr2)
print(newarr)  # [5 7 9]

arr3 = np.array([1, 2, 3])
arr4 = np.array([1, 2, 3])
newarr2 = np.sum([arr3, arr4])
print(newarr2)  # 12

arr5 = np.array([1, 2, 3])
arr6 = np.array([1, 2, 3])
newarr3 = np.sum([arr5, arr6], axis=1)
print(newarr3)  # [6 6]

arr7 = np.array([1, 2, 3, 4])
newarr4 = np.cumsum(arr7)
print(newarr4)  # [ 1  3  6 10]
# [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10]
