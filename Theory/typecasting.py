# Typecasting - converting one data type to another
#               str(), int(), float(), bool()

name = ""
age = 18
gpa = 3.6
isStudent = True

print(f"Type of int converted to float -- {type(float(age))}")
print(f"0 converted to bool -- {bool(0)}")  # output is False
print(f"Empty str converted to bool -- {bool(name)}")  # output is False
print(f"Bool converted to int -- {int(isStudent)}")  # output is 1
