pairs = [(1, 5), (3, 9), (10, 2), (4, 4)]

max_pair = None
max_sum = 0

for pair in pairs:
    current_sum = pair[0] + pair[1]
    if current_sum > max_sum:
        max_sum = current_sum
        max_pair = pair

print("Tuple with max sum:", max_pair)