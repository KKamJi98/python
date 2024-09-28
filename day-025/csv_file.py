import os
import csv

PATH = os.path.join((os.path.dirname(__file__)), "weather_data.csv")


# with open(PATH, mode="r") as file:
#     temp_data = file.readlines()
#     data = []
#     for line in temp_data:
#         data.append(line.strip().split(","))
#     print(data)
    

with open(PATH) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        print(row)
        if row[1].isdigit():
            temperatures.append(int(row[1]))
    print(temperatures)
            