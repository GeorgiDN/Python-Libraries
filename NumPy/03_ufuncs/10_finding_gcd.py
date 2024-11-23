import numpy as np

# Greatest Common Denominator
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)


arr = np.array([20, 8, 32, 36, 16])
x2 = np.gcd.reduce(arr)
print(x2)  # 4
