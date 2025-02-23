# c = 2piR
# s = piR^2
from Lessons import math

r = float(input("Enter the radius: "))

c = 2 * math.pi * r
s = math.pi * pow(r, 2)

print(f"The length of the circle is: {round(c, 2)}")
print(f"The area of the circle is: {round(s, 2)}")


