import numpy as np

# Example
# Without ufunc, can use Python's built-in zip()
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
    z.append(i + j)
print(z)


print()
# add()
x2 = [1, 2, 3, 4]
y2 = [4, 5, 6, 7]
z2 = np.add(x, y)
print(z2)
