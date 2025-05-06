# 90 or higher
grades = {"Anna": 92, "David": 85, "Maria": 97, "John": 88, "Sophia": 90}
filteredGrades = {}

items = grades.items()

for key, value in items:
    if value >= 90:
        filteredGrades.update({key: value})

print(filteredGrades)
