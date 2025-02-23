weight = float(input("Enter your weight: "))
unit = input("Choose unit (K - Kilogram, L - Pound) ")

if unit == "K":
    weight *= 2.2025
    unit = "Lbs"
    print(f"Your weight is {round(weight, 2)}{unit}")
elif unit == "L":
    weight /= 2.2025
    unit = "Kgs"
    print(f"Your weight is {round(weight, 2)}{unit}")
else:
    print(f"{unit} is not valid:")
