pairs = [(2, 5), (3, 7), (6, 6), (4, 9)]
max_product_pair = max(pairs, key=lambda x: x[0]*x[1])
print("Tuple with max product:", max_product_pair)