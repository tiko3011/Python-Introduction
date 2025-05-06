data = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8]
seen = set()
duplicates = set()
setData = set(data)

for i in data:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(f"Duplicates: {duplicates}")
print(f"Only once: {seen - duplicates}")
print(f"Data: {setData}")


# Որ տարրերն են կրկնվում,
# Որ տարրերն են հանդիպում միայն մեկ անգամ,
# Եվ բոլոր եզակի տարրերը (առանց կրկնության)։