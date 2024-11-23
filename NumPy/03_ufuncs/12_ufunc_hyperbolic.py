import numpy as np

# Hyperbolic Functions
x = np.sinh(np.pi/2)
print(x)  #


arr2 = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x2 = np.cosh(arr2)
print(x2)  # [2.50917848 1.60028686 1.32460909 1.20397209]


# Finding Angles
x3 = np.arcsinh(1.0)
print(x3)  # 0.881373587019543


arr3 = np.array([0.1, 0.2, 0.5])
x4 = np.arctanh(arr3)
print(x4)  # [0.10033535 0.20273255 0.54930614]
