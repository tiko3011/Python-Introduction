dept_a = {"Anna", "Boris", "Charlie", "Diana"}
dept_b = {"Boris", "Diana", "Edward", "Fiona"}
dept_c = {"Charlie", "Diana", "George", "Helen"}

# Find common employees
all_three = dept_a & dept_b & dept_c

# Find employees in at least two departments
two_or_more = (dept_a & dept_b) | (dept_a & dept_c) | (dept_b & dept_c)

# Find employees in only one department
only_one = (dept_a | dept_b | dept_c) - two_or_more

print("In all three:", all_three)
print("In at least two:", two_or_more)
print("Only in one:", only_one)