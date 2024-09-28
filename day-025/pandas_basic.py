import pandas
import os

PATH = os.path.join(os.path.dirname(__file__), "weather_data.csv")

data = pandas.read_csv(PATH)
# print(data["condition"]) # 컬럼네임으로 해당 컬럼 조회 가능
# print(data.condition)
print(type(data["temp"]))

# print(data)
# '''
#          day  temp condition
# 0     Monday    22     Sunny
# 1    Tuesday    25    Cloudy
# 2  Wednesday    27     Rainy
# 3   Thursday    20     Sunny
# 4     Friday    23     Rainy
# 5   Saturday    26    Cloudy
# 6     Sunday    24     Sunny
# '''

# DataFrame to Dictionary
data_dict = data.to_dict()
# print(data_dict)

# 평균 온도 계산해보기 ver1
# temp_list = data["temp"].to_list()
# total_temp = sum(temp_list)
# temp_list_length = len(temp_list)
# print(f"average temperature => {total_temp/temp_list_length:.2f}")

# 평균 온도 계산해보기 ver2 (Pandas 메소드 사용)

# average_temp = data["temp"].mean()
# print(f"average temperature => {average_temp:.2f}")

# 최고 온도 찾기
# print(data["temp"].max())

# 최고 온도가 있는 행 추출
print(data[data.temp == data["temp"].max()])


#####################

# 월요일의 온도를 불러오는데 온도를 화씨로 표시
monday = data[data.day == "Monday"]
monday_temp = monday.temp.iloc[0]
monday_temp_fahrenheit = monday_temp * 9/5 + 32
print(f"Monday's temperature in Fahrenheit: {monday_temp_fahrenheit:.2f}")