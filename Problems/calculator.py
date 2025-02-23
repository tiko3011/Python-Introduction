x = float(input("Enter the first number: "))
operator = input("Choose the operator (+, -, /, *): ")
y = float(input("Enter the first number: "))

if operator == "+":
    print(f"{x} {operator} {y} = {x + y}")
elif operator == "-":
    print(f"{x} {operator} {y} = {x - y}")
elif operator == "*":
    print(f"{x} {operator} {y} = {x * y}")
elif operator == "/":
    print(f"{x} {operator} {y} = {round(x / y, 2)}")
else:
    print("Yoo are you retarded?")
