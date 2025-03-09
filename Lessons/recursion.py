# ITERATION
# def walk(steps):
#     for step in range(1, steps + 1):
#         print(f"You take step #{step}")

# RECURSION
# def walk(steps):
#     if steps == 0:
#         return
#     walk(steps - 1)
#     print(f"You take step #{steps}")
# walk(100)

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return x * factorial(x - 1)

# def sumOfDigits(x):
#     if x == 0:
#         return 0
#     else:
#         return x % 10 + sumOfDigits(x // 10)

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)