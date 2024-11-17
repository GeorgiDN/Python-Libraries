import numpy as np

# Join two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_1_2 = np.concatenate((arr1, arr2))
print(arr_1_2)


print()
# Join two 2-D arrays along rows (axis=1):
arr3 = np.array([[1, 2], [5, 6]])
arr4 = np.array([[3, 4], [7, 8]])
arr_3_4 = np.concatenate((arr3, arr4), axis=1)
print(arr_3_4)


print()
# Joining Arrays Using Stack Functions
arr5 = np.array([1, 2, 3])
arr6 = np.array([4, 5, 6])
arr_5_6 = np.stack((arr5, arr6), axis=1)
print(arr_5_6)


print()
# Stacking Along Rows
# hstack() to stack along rows.
arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])
arr_7_8 = np.hstack((arr7, arr8))
print(arr_7_8)


print()
# Stacking Along Columns
# vstack()  to stack along columns.
arr9 = np.array([1, 2, 3])
arr10 = np.array([4, 5, 6])
arr_9_10 = np.vstack((arr9, arr10))
print(arr_9_10)


print()
# Stacking Along Height (depth)
# dstack() to stack along height, which is the same as depth.#
arr11 = np.array([1, 2, 3, 4])
arr12 = np.array([5, 7, 8, 9])
arr_11_12 = np.dstack((arr11, arr12))
print(arr_11_12)
