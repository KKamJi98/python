student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

student_grades = {}

for key in student_scores:
    grade = str()
    value = student_scores[key]
    if value > 90 and value <= 100:
        grade = "Outstanding"
    elif value > 80:
        grade = "Exceeds Expectations"
    elif value > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade

print(student_grades)
