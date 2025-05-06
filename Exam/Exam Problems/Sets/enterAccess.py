dept_a = {"Anna", "Boris", "Charlie", "Diana"}
dept_b = {"Boris", "Diana", "Edward", "Fiona"}
dept_c = {"Charlie", "Diana", "George", "Helen"}

access3 = dept_a & dept_b & dept_c
accessAtLeast2 = (dept_a & dept_b) | (dept_c & dept_a) | (dept_c & dept_b)
access1 = (dept_a | dept_b | dept_c) - accessAtLeast2

print(access3)
print(accessAtLeast2)
print(access1)
