data = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8]

# Find duplicates
duplicates = []
seen = set()
for num in data:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)

# Find unique elements (appearing once)
unique_once = [num for num in seen if data.count(num) == 1]

print("Duplicates:", duplicates)
print("Unique elements (once):", unique_once)
print("All unique elements:", list(seen))