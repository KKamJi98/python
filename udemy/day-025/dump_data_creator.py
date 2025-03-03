import pandas as pd
import os

PATH = os.path.join(os.path.dirname(__file__), "weather_data.csv")

data = {
    "day": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ],
    "temp": [22, 25, 27, 20, 23, 26, 24],
    "condition": ["Sunny", "Cloudy", "Rainy", "Sunny", "Rainy", "Cloudy", "Sunny"],
}

df = pd.DataFrame(data)

csv_file_path = "/mnt/data/weather_data.csv"
df.to_csv(PATH, index=False)
