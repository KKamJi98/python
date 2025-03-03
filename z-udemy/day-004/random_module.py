import random

# 1이상 10이하 랜덤 정수 난수 생성
random_integer = random.randint(1, 10)
print(random_integer)

# 0이상 1미만 부동 소수점 난수 생성
random_float = random.random()
print(random_float)

# 0이상 5이하 부동 소수점 난수 생성
random_float2 = random.uniform(0, 5)
print(random_float2)
