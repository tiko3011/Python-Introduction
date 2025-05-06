dept_a = {"Anna", "Boris", "Charlie", "Diana"}
dept_b = {"Boris", "Diana", "Edward", "Fiona"}
dept_c = {"Charlie", "Diana", "George", "Helen"}

all_three = dept_a & dept_b & dept_c
at_least_two = (dept_a & dept_b) | (dept_a & dept_c) | (dept_b & dept_c)
only_one = (dept_a ^ dept_b ^ dept_c) - at_least_two

print("All three departments:", all_three)
print("At least two departments:", at_least_two)
print("Only one department:", only_one)