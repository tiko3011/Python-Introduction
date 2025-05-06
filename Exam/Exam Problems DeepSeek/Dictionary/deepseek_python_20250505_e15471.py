d1 = {"a": 10, "b": 5, "c": 2}
d2 = {"b": 3, "c": 8, "d": 7}

result = {}

# Add all keys from both dictionaries
for key in d1:
    result[key] = d1[key]
    
for key in d2:
    if key in result:
        result[key] += d2[key]
    else:
        result[key] = d2[key]

print("Merged dictionary:", result)