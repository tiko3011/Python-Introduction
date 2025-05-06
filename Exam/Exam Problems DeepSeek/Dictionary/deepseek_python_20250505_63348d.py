d1 = {"a": 10, "b": 5, "c": 2}
d2 = {"b": 3, "c": 8, "d": 7}
merged = {k: d1.get(k,0) + d2.get(k,0) for k in set(d1)|set(d2)}
print("Merged dictionary:", merged)