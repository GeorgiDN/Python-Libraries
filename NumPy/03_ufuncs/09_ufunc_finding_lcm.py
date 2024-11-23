import numpy as np

# Lowest Common Multiple
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)  # 12


# Finding LCM in Arrays
arr = np.array([3, 6, 9])
x2 = np.lcm.reduce(arr)
print(x2)  # 18
# 3*6=18, 6*3=18 and 9*2=18


arr2 = np.arange(1, 11)
x3 = np.lcm.reduce(arr2)
print(x3)  # 2520
