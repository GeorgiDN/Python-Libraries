import pandas as pd


def print_delimiter(header):
    print(f"------------------------------ {header} ------------------------------")


def p():
    print()


data = {
    "Duration": [60, 60, None],
    "Date": ['2020/12/01', None, '2020/12/03'],
    "Pulse": [110, 117, None],
    "Maxpulse": [130, None, 135],
    "Calories": [409.1, None, 340.0]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

p()

print_delimiter("isnull")
print(df.isnull())


p()
print_delimiter("dropna")
df_cleaned = df.dropna()  # Removes any row with at least one NaN
print(df_cleaned)


p()
print_delimiter("fillna")
# Fill missing values with a specific value
df_filled = df.fillna(0)
print(df_filled)

p()
print_delimiter("fillna df.mean(numeric_only=True")
# Fill missing values with column means (for numeric columns)
df_filled = df.fillna(df.mean(numeric_only=True))
print(df_filled)


p()
print_delimiter("isnull().sum()")
print(df.isnull().sum())  # Count NaN values in each column
