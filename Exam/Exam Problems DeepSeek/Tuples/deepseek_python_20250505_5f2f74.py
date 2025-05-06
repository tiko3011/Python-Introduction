pairs = [(1, 5), (10, 2), (3, 9), (6, 15)]

max_diff_pair = None
max_diff = 0

for pair in pairs:
    current_diff = abs(pair[0] - pair[1])
    if current_diff > max_diff:
        max_diff = current_diff
        max_diff_pair = pair

print("Tuple with max difference:", max_diff_pair)