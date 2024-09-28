import pandas
import os

# PATH = os.path.join(os.path.dirname(__file__), "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
PATH = os.path.dirname(__file__)

data = pandas.read_csv(PATH + "/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# primary_fur_color = data["Primary Fur Color"]
# print(primary_fur_color)

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]
# print(gray_squirrels)
grey_squirrels_count = len(gray_squirrels)
red_squirrels_count = len(red_squirrels)
black_squirrels_count = len(black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv(PATH + "/squirrel_count.csv")
