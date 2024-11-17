from numpy import random

x = random.randint(10)
print(x)


print()
# Generate a random float from 0 to 1:
x2 = random.rand()
print(x2)


print()
# Generate a 1-D array containing 6 random integers from 0 to 49:
x3 = random.randint(49, size=6)
print(x3)


print()
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x4 = random.randint(100, size=(3, 5))
print(x4)


print()
# Generate a 1-D array containing 5 random floats:
x5 = random.rand(5)
print(x5)


print()
# Generate a 2-D array with 3 rows, each row containing 5 random numbers:
x6 = random.rand(3, 5)
print(x6)


print()
# Return one of the values in an array:
x7 = random.choice([3, 5, 7, 9])
print(x7)


print()
# Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9):
x8 = random.choice([3, 5, 7, 9], size=(3, 5))
print(x8)
