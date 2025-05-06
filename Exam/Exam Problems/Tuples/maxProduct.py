pairs = [(2, 5), (3, 7), (6, 6), (4, 9)]

maxProductTuple = max(pairs, key=lambda x: x[0] * x[1])
maxProduct = maxProductTuple[0] * maxProductTuple[1]

for pair in pairs:
    if pair[0] * pair[1] == maxProduct:
        print(pair)

print(maxProduct)