import pandas as pd

# Create a DataFrame with the example data
data = {
    "Duration": [60, 60, 60],
    "Date": ['2020/12/01', '2020/12/02', '2020/12/03'],
    "Pulse": [110, 117, 103],
    "Maxpulse": [130, 145, 135],
    "Calories": [409.1, 479.0, 340.0]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)
