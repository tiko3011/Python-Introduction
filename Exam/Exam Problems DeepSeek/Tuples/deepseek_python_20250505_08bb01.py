pairs = [(1, 5), (3, 9), (10, 2), (4, 4)]
max_pair = max(pairs, key=lambda x: sum(x))
print("Tuple with max sum:", max_pair, "Sum:", sum(max_pair))