import numpy as np

# Trunc
arr = np.trunc([-3.1666, 3.6667])
print(arr)  # [-3.  3.]


print()
# Fix
arr = np.fix([-3.1666, 3.6667])
print(arr)   # [-3.  3.]


print()
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
arr = np.around(3.1666, 2)
print(arr)  # 3.17


print()
# Floor
arr = np.floor([-3.1666, 3.6667])
print(arr)  # [-4.  3.]


print()
# Ceil
arr = np.ceil([-3.1666, 3.6667])
print(arr)  # [-3.  4.]
