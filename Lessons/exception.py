# try:
#     # Try some code
# except Exception:
#     # Handle exception
# finally:
#     # Do some cleanup
try:
    x = int(input("Enter number: "))
    print(1 / x)
except ZeroDivisionError:
    print("Cant divide by 0!")
    x = int(input("Enter number: "))
    print(1 / x)
except ValueError:
    print("Enter only number! Idiot")
    x = int(input("Enter number: "))
    print(1 / x)
finally:
    print("Cool")


