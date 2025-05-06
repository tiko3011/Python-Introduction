d1 = {"a": 10, "b": 5, "c": 2}
d2 = {"b": 3, "c": 8, "d": 7}
d3 = {}

keys1 = d1.keys()
keys2 = d2.keys()

for key1 in keys1:
    isDuplicate = False
    for key2 in keys2:
        isDuplicate = False
        if key1 == key2:
            d3.update({key1: d1.get(key1) + d2.get(key2)})
            isDuplicate = True
            break
    if not isDuplicate:
        d3.update({key1: d1.get(key1)})

keys3 = d3.keys()

for key2 in keys2:
    isDuplicate = False
    for key1 in keys1:
        isDuplicate = False
        if key2 == key1:
            isDuplicate = True
            break
    if not isDuplicate:
        d3.update({key2: d2.get(key2)})

print(d3)

