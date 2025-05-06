name = input("What is your name? ")
age = int(input("How old are you? "))

isUnderage = age < 18

if isUnderage:
    print(f"Hi {name}! You can't buy weed")
else:
    print(f"Hi {name}! Deposit 23$ to EasyPay")


