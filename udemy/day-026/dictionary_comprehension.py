# new_dict = [new_key:new_value for item in list]
# new_dict = {new_key:new_value for (key, value) in dict.items()}

# student_score: dict[str, int] = {
#     "Alex": 89,
#     "Beth": 92,
#     "Caroline": 78,
#     "Dave": 65,
#     "Eleanor": 93,
#     "Freddie": 88
# }
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

print(student_score.items())

passed_student = {name: score for (name, score) in student_score.items() if score >= 60}
print(passed_student)
