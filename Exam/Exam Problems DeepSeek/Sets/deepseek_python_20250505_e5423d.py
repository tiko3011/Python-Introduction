from collections import Counter

data = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8]
counts = Counter(data)

repeated = [k for k, v in counts.items() if v > 1]
unique_once = [k for k, v in counts.items() if v == 1]
all_unique = list(counts.keys())

print("Repeated elements:", repeated)
print("Elements appearing once:", unique_once)
print("All unique elements:", all_unique)