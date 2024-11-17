import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>


print()
arr2 = np.array((1, 2, 3, 4, 5))
print(arr2)  # [1 2 3 4 5]


print()
zero_d_arr = np.array(42)
print(zero_d_arr)  # 42


print()
one_d_arr = np.array([1, 2, 3, 4, 5])
print(one_d_arr)  # [1 2 3 4 5]


print()
two_d_arr = np.array([[1, 2, 3], [4, 5, 6]])
print(two_d_arr)


print()
three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(three_d_arr)
