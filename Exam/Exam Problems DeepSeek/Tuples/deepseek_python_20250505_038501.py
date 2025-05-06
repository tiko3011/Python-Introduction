pairs = [(2, 4), (6, 8), (10, 12), (14, 17), (20, 18)]

# Filter even-numbered pairs
even_pairs = []
for a, b in pairs:
    if a % 2 == 0 and b % 2 == 0:
        even_pairs.append((a, b))

# Find pair with smallest difference
min_diff_pair = None
min_diff = float('inf')
for pair in even_pairs:
    diff = abs(pair[0] - pair[1])
    if diff < min_diff:
        min_diff = diff
        min_diff_pair = pair

print("Even pairs:", even_pairs)
print("Pair with smallest difference:", min_diff_pair)