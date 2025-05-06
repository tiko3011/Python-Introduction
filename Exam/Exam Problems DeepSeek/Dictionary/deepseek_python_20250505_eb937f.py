grades = {'Anna': 92, 'David': 85, 'Maria': 97, 'John': 88, 'Sophia': 90}

# Filter top students
top_students = {}
for name, grade in grades.items():
    if grade >= 90:
        top_students[name] = grade

print("Top students:", top_students)