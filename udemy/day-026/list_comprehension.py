# new_list = [new_item for item in list]


## List Comprehension

numbers: list[int] = [1, 2, 3]

new_numbers: list[int] = [ele + 1 for ele in numbers]
print(new_numbers)

new_numbers2: list[int] = [ele * 2 for ele in range(1, 5)]
print(new_numbers2)

# Conditional List Comprehension

names: list[str] = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# 이름의 길이가 다섯 글자 미만인 것으로 리스트에 조건부 추가
short_names = [name for name in names if len(name) < 5]
print(short_names)

# 이름의 길이가 다섯 글자 이상인 이름을 모두 가져오기
long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)
