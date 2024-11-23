import numpy as np

# Trigonometric Functions
x = np.sin(np.pi/2)
print(x)  # 1.0


arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x2 = np.sin(arr)
print(x2)  # [1.         0.8660254  0.70710678 0.58778525]


# Convert Degrees Into Radians
arr2 = np.array([90, 180, 270, 360])
x3 = np.deg2rad(arr2)
print(x3)  # [1.57079633 3.14159265 4.71238898 6.28318531]
#  r = d * (pi / 180)


# Radians to Degrees

arr3 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x4 = np.rad2deg(arr3)
print(x4)  # [ 90. 180. 270. 360.]
# d = r * (180 / pi)


# Finding Angles
x5 = np.arcsin(1.0)
print(x5)  # 1.5707963267948966
# pi / 2


arr4 = np.array([1, -1, 0.1])
x6 = np.arcsin(arr4)
print(x6)  # [ 1.57079633 -1.57079633  0.10016742]


# Hypotenues
base = 3
perp = 4
x7 = np.hypot(base, perp)
print(x7)  # 5.0
