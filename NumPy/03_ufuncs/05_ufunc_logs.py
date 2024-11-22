import numpy as np
from math import log

arr = np.arange(1, 10)
print(np.log2(arr))

print(np.log2(3))  # 1.5849625
print()
print(2 ** 1.5849625)  # 3

print()
arr2 = np.arange(1, 10)
print(np.log10(arr2))


print()
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))  # 1.7005483074552052
print(15 ** 1.7005483074552052)  # 100


