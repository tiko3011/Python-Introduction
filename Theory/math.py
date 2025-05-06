import math

dollars = 5
dollars = dollars ** 2  # dollars = dollars * dollars (6*6=36)

x = 3.14
y = -4
z = 5

result = round(x)
print(f"Round 3.14 -> {result}")  # 3.14 -> 3
result = round(x, 1)
print(f"Round 3.14 1 digit -> {result}")  # 3.14 -> 3.1

result = abs(y)
print(f"Abs -4 -> {result}")  # -4 -> 4

result = pow(z, 2)
print(f"Pow(5, 2) -> {result}")  # z^2 = 25

result = max(x, y, z)
print(f"Max(3.14, -4, 5) -> {result}")

result = min(x, y, z)
print(f"Min(3.14, -4, 5) -> {result}")

result = math.sqrt(9)
print(f"Sqrt 9 -> {result}")

result = math.ceil(x)
print(f"Ceil 3.14 -> {result}")

result = math.floor(9.9)
print(f"Floor 9.9 -> {result}")

print(f"{math.pi}")
