import pandas as pd


def print_delimiter(header):
    print()
    print(f"------------------------------ {header} ------------------------------")


# Load the Excel file into a DataFrame
df = pd.read_excel("employee_data.xlsx")


print_delimiter("MIN, MAX, AVERAGE")
# Minimum Salary
print("Minimum Salary:", df["Salary"].min())

# Maximum Salary
print("Maximum Salary:", df["Salary"].max())

# Average Salary
print("Average Salary:", df["Salary"].mean())


print_delimiter("-----SORT----")
print_delimiter("Sort by Salary (Ascending)")

# Sort by Salary (Ascending)
sorted_by_salary_asc = df.sort_values(by="Salary", ascending=True)
print(sorted_by_salary_asc)


print_delimiter("Sort by Age (Descending):")
# Sort by Age (Descending):
sorted_by_age_desc = df.sort_values(by="Age", ascending=False)
print(sorted_by_age_desc)


print_delimiter("Sort by Department (Alphabetically) and Salary (Descending):")
# Sort by Department (Alphabetically) and Salary (Descending):
sorted_df = df.sort_values(by=["Department", "Salary"], ascending=[True, False])
print(sorted_df)
