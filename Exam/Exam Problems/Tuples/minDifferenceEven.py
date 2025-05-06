pairs = [(2, 4), (6, 8), (10, 12), (14, 17), (20, 18)]
evenPairs = []

for pair in pairs:
    if pair[0] % 2 == 0 and pair[1] % 2 == 0:
        evenPairs.append(pair)

minAbsDifferenceTuple = min(evenPairs, key=lambda x: abs(x[0] - x[1]))
minAbsDifference = abs(minAbsDifferenceTuple[0] - minAbsDifferenceTuple[1])

for pair in evenPairs:
    if abs(pair[0] - pair[1]) == minAbsDifference:
        print(pair)

print(minAbsDifference)