# exception --> events detected during reading the program
#               that interrupt the flow of a program

try:
    numerator = int(input("Enter the numerator to divide: "))
    denominator = int(input("Enter the denominator to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("Can't divide by 0")
except ValueError as e:
    print(e)
    print("Enter ONLY numbers please")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    # Close the files
    print("End of the program")

