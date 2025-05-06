students = {"Alice": 101, "Bob": 102, "Clara": 103}

swapped = {}
for name, id in students.items():
    swapped[id] = name

print("Swapped dictionary:", swapped)