pairs = [(1, 5), (3, 9), (10, 2), (4, 4), (12, 0)]

maxPair = (max(pairs, key=lambda x: x[0] + x[1]))
maxSum = maxPair[0] + maxPair[1]

for pair in pairs:
    if pair[0] + pair[1] == maxSum:
        print(pair)