import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr_copy = arr.copy()
arr[0] = 42
print(arr)  # [42  2  3  4  5]
print(arr_copy)  # [1 2 3 4 5]


print()
arr2 = np.array([1, 2, 3, 4, 5])
arr_view = arr2.view()
arr2[0] = 42
print(arr2)  # [42  2  3  4  5]
print(arr_view)  # [42  2  3  4  5]


print()
arr3 = np.array([1, 2, 3, 4, 5])
x = arr3.view()
x[0] = 31
print(arr3)
print(x)


print()
# Check if an array owns it's data or not:
arr = np.array([1, 2, 3, 4, 5])
a = arr.copy()
b = arr.view()
print(a.base)  # None
print(b.base)  # [1 2 3 4 5]
