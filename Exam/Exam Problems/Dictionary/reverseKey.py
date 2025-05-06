students = {"Alice": 101, "Bob": 102, "Clara": 103}
reverseStudents = {}

items = students.items()

for key, value in items:
    reverseStudents.update({value: key})

print(reverseStudents)