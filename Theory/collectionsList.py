# Collection = single "variable" used to store multiple values
#   List   = [] ordered and changeable. Duplicates OK
#   Set    = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple  = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["Apple", "Banana", "Coconut"]

# print(fruits[-1])  -> Coconut
# print(fruits[::2]) -> ['Apple', 'Coconut']

# isAppleIn = "Apple" in fruits
# isPineappleIn = "Pineapple" in fruits
# print(f"Apple: {isAppleIn}")
# print(f"Pineapple: {isPineappleIn}")

for i in fruits:
    print(i)

# fruits[0] = "Pineapple"
# for i in range(len(fruits)):
#     print(i)

fruits.append("Watermelon")  # To the end of the list
print(f"Added Watermelon: {fruits}")

fruits.insert(0, "Pomegranate")
print(f"Added Pomegranate to start: {fruits}")

fruits.remove("Apple")
fruits.pop()
print(f"Removed Apple and Last item: {fruits}")

fruits.sort()
print(f"Sorted: {fruits}")

fruits.reverse()
print(f"Reversed: {fruits}")

index = fruits.index("Pomegranate")
print(f"Pomegranate index: {index}")

fruits.clear()
print(f"Cleared list: {fruits}")


