pairs = [(1, 5), (10, 2), (3, 9), (6, 15)]

maxAbsDifferenceTuple = max(pairs, key=lambda x: abs(x[0] - x[1]))
maxAbsDifference = abs(maxAbsDifferenceTuple[0] - maxAbsDifferenceTuple[1])

for pair in pairs:
    if abs(pair[0] - pair[1]) == maxAbsDifference:
        print(pair)