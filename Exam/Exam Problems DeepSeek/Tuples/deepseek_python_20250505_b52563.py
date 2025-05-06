pairs = [(2, 4), (6, 8), (10, 12), (14, 17), (20, 18)]
even_pairs = [p for p in pairs if p[0]%2==0 and p[1]%2==0]
min_diff_pair = min(even_pairs, key=lambda x: abs(x[0] - x[1]))
print("Selected even tuple with min difference:", min_diff_pair)