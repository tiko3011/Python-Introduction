grades = {'Anna': 92, 'David': 85, 'Maria': 97, 'John': 88, 'Sophia': 90}
filtered = {k:v for k,v in grades.items() if v >= 90}
print("Students with A grade:", filtered)