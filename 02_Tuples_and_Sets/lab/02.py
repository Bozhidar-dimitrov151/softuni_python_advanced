number_students = int(input())

grades = {}

for _ in range(number_students):
    student, grade = input().split()
    if grades.get(student) is None:
        grades[student] = []

    grades[student].append(float(grade))

for student, grades_list in grades.items():
    current_grades = " ".join(f"{x:.2f}" for x in grades_list)
    print(f"{student} -> {current_grades} (avg: {sum(grades_list)/len(grades_list):.2f})")
