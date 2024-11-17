import pandas as pd

nums = [1, 7, 2]

series = pd.Series(nums, index=["x", "y", "z"])

print(series)
print(series["y"])

print()
calories = {"day1": 420, "day2": 380, "day3": 390}
calories_series = pd.Series(calories)
print(calories_series)
print(calories_series["day1"])
print()

print(pd.Series(calories, index=["day1", "day2"]))
