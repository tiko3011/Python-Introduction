pairs = [(2, 5), (3, 7), (6, 6), (4, 9)]

max_product = 0
result_pair = None

for a, b in pairs:
    product = a * b
    if product > max_product:
        max_product = product
        result_pair = (a, b)

print(f"Tuple with max product: {result_pair} (Product = {max_product})")