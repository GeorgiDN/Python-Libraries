import pandas as pd

# Load the JSON file into a DataFrame
df = pd.read_json("example1.json")

# Display the DataFrame
print(df)

print()
print("Info")
# Optional: Display summary information
print(df.info())

print()
print(df.to_string())

print()
print("----------------------------------------------------------------------------------")
data2 = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}

df2 = pd.DataFrame(data2)

print(df2)
