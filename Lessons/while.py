# while loop -> do smth WHILE condition is true

food = input("Enter a food you like (Press 'q' to quit): ")

while not food == "q":
    print(f"You like {food}:")
    food = input("Enter another food you like: ")

print("BYE!")