import pandas
import os

PATH = os.path.join(os.path.dirname(__file__), "new_data.csv")

data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 65]}

data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv(PATH)
