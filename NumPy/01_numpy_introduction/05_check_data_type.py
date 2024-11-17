import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)  # int64


print()
arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)  # <U6


print()
arr3 = np.array([1, 2, 3, 4], dtype='S')
print(arr3)  # [b'1' b'2' b'3' b'4']
print(arr3.dtype)  # |S1


print()
arr4 = np.array([1, 2, 3, 4], dtype='i4')
print(arr4)  # [1 2 3 4]
print(arr4.dtype)  # int32


print()
# Change data type from float to integer by using 'i' as parameter
ar5 = np.array([1.1, 2.1, 3.1])
newarr = ar5.astype('i')
print(newarr)  # [1 2 3]
print(newarr.dtype)  # int32


print()
arr6 = np.array([1.1, 2.1, 3.1])
newarr2 = arr6.astype(int)
print(newarr2)  # [1 2 3]
print(newarr2.dtype)  # int64


print()
arr7 = np.array([1, 0, 3])
newarr3 = arr7.astype(bool)
print(newarr3)  # [ True False  True]
print(newarr3.dtype)  # bool
