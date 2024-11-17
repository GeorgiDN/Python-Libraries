import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


df = pd.DataFrame(data)

print(df.loc[0])
print(df.loc[[0, 1]])

print()
data2 = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df2)
