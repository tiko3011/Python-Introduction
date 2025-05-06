pairs = [(1, 5), (10, 2), (3, 9), (6, 15)]
max_diff_pair = max(pairs, key=lambda x: abs(x[0] - x[1]))
print("Tuple with max absolute difference:", max_diff_pair)