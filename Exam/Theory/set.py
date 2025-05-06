# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates

dept_a = {"Anna", "Boris", "Charlie", "Diana"}
dept_b = {"Boris", "Diana", "Edward", "Fiona"}
dept_c = {"Charlie", "Diana", "George", "Helen"}

print(dept_a)
print("Tigran" in dept_a)

dept_a.add("Sahak")
dept_a.remove("Boris")
print(dept_a)


