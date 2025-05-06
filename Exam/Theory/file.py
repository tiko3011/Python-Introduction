# "r" - read
# "w" - write
# "x" - write if it doesn't exist (error if exists)
# "a" - append

###############################################################

# Reading python files

file_path = "txt/reading.txt"

try:
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())  # strip() removes the newline character
        file.seek(0)  # move cursor to the start
        content = file.read()
        # print(content)
except FileNotFoundError:
    print("Wrong File Path")

###############################################################

# Writing python files

employees = ["Bounty", "Twix", "Snickers"]

content = "Some Random Info"
file_path = "txt/writing.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(f"{employee}\n")
        print(f"File '{file_path}' was created")
except FileNotFoundError:
    print("Wrong File Path")
