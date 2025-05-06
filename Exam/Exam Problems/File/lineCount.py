file_path = "txt/data.txt"
line_count = 0

try:
    with open(file_path, "r") as file:
        for line in file:
            print(line.strip())
            line_count += 1
except FileNotFoundError:
    print("File does not exist, please provide existing file path")
else:
    print(line_count)


