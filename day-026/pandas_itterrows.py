"""
- Dictionary는 items() 메소드로 반복 가능하며, DataFrame도 비슷한 방식으로 반복 가능
- DataFrame의 각 행을 반복하려면 iterrows() 메소드를 사용해야함.
- 특정 행의 값을 조회할 때는 점 표기법을 사용해 열 이름으로 접근.
- 조건문을 사용해 특정 값을 가진 행 출력 가능
"""

student_dict = {"student": ["Angela", "James", "Lily"], "score": [56, 76, 98]}

for key, value in student_dict.items():
    print(key)  # 키 출력
    print(value)  # 값 출력

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

for key, value in student_data_frame.items():
    print(key)  # 열 이름 출력
    print(value)  # 각 열에 해당하는 데이터 출력

# iterrows() 메소드를 사용한 행 반복
for index, row in student_data_frame.iterrows():
    print(index)  # 인덱스 출력
    print(row)  # 각 행의 데이터 출력

# 행 데이터 접근
for index, row in student_data_frame.iterrows():
    print(row.student)  # 학생 이름 출력
    print(row.score)  # 점수 출력

# 조건문을 사용해 특정 행 조회. (특전 조건을 만족하는 행만 선택)
for index, row in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)  # Angela의 점수 출력
