from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)


print()
# Generate a random permutation of elements of following array:
arr2 = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr2))
print(arr2)


