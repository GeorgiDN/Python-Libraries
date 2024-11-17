import pandas as pd


def print_delimiter(header):
    print()
    print(f"------------------------------ {header} ------------------------------")


data1 = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [30, 25, 35, 28, 40],
    "Country": ["USA", "UK", "Canada", "Australia", "France"]
}

data2 = {
    "Product": ["Laptop", "Tablet", "Smartphone", "Monitor", "Keyboard"],
    "Price": [1000, 500, 700, 300, 50],
    "Stock": [50, 100, 150, 75, 200]
}

# Convert data to DataFrames
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# # # Write data to an Excel file with multiple sheets
# with pd.ExcelWriter("example.xlsx") as writer:
#     df1.to_excel(writer, sheet_name="Sheet1", index=False)
#     df2.to_excel(writer, sheet_name="Sheet2", index=False)
#
#
# # # Write a DataFrame to a new Excel file
# df1.to_excel("new_file.xlsx", sheet_name="People", index=False)
#
#
# # # Add a new column to a DataFrame
# df1["Salary"] = [50000, 55000, 60000, 48000, 52000]
#
# # # Save the modified DataFrame back to the file
# with pd.ExcelWriter("example_modified.xlsx", mode="a") as writer:  # Append mode
#     df1.to_excel(writer, sheet_name="UpdatedSheet1", index=False)


# print_delimiter("Filter rows based on conditions")
# # Filter rows based on conditions
# adults = df1[df1["Age"] > 30]
# print(adults)
#
# # Summarize data
# print(df1.describe())  # Summary statistics for numeric columns


# data_with_na = {
#     "Name": ["Alice", "Bob", None],
#     "Age": [30, None, 35],
#     "Country": ["USA", None, "Canada"]
# }
#
# #  Handle Missing Data in Excel
# df_with_na = pd.DataFrame(data_with_na)
# df_with_na.to_excel("example_with_na.xlsx", index=False)
#
# # Fill missing values
# df_filled = df_with_na.fillna("Unknown")
# print_delimiter("Fill missing values")
# print(df_filled)


# print_delimiter("Read only specific columns")
# # Read only specific columns
# df_subset = pd.read_excel("example.xlsx", sheet_name="Sheet1", usecols=["Name", "Age"])
# print(df_subset)
#
# print_delimiter("Read specific rows by skipping rows")
# # Read specific rows by skipping rows
# df_skipped = pd.read_excel("example.xlsx", sheet_name="Sheet1", skiprows=1, nrows=3)
# print(df_skipped)



# Load all sheets into a dictionary
all_sheets = pd.read_excel("example.xlsx", sheet_name=None)
combined_df = pd.concat([all_sheets["Sheet1"], all_sheets["Sheet2"]], axis=0, ignore_index=True)
print(combined_df)


# # Pivot tables
# print_delimiter("Pivot table")
# pivot_table = df2.pivot_table(values="Price", index="Stock", aggfunc="mean")
# print(pivot_table)

