import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
    print(x)


print()
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr2:
    print(x)


print()
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr3:
    for y in x:
        print(y)


print()
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr4:
    print(x)


print()
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr5:
    for y in x:
        for z in y:
            print(z)


# Iterating Arrays Using nditer()
print()
arr6 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr6):
    print(x)


print()
# Iterating Array With Different Data Types
arr7 = np.array([1, 2, 3])
for x in np.nditer(arr7, flags=['buffered'], op_dtypes=['S']):
    print(x)


print()
# Iterating With Different Step Size
arr8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr8[:, ::2]):
    print(x)


print()
# Enumerated Iteration Using ndenumerate()
arr9 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr9):
    print(idx, x)


print()
# Enumerate on following 2D array's elements:
arr10 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr10):
    print(idx, x)
