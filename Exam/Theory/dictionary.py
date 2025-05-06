# dictionary =  a collection {key:value} pairs
#               ordered and changeable. No duplictaes

capitals = {"USA": "Washington",
            "Armenia": "Erevan",
            "Russia": "Moscow"}

# print(capitals.get("USA"))
# print(capitals.get("Japan"))  # Doesn't exist -> None

capitals.update({"Germany": "Berlin"})  # Add
capitals.update({"USA": "Detroit"})  # Change
capitals.pop("Russia")  # Remove
capitals.popitem()  # Remove latest item

print(capitals)

keys = capitals.keys()
for key in keys:
    print(key)

values = capitals.values()
for value in values:
    print(value)

items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key} - {value}")


