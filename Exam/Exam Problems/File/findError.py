file_path = "txt/log.txt"
text = "error"

try:
    with open(file_path, "r") as file:
        for line in file:
            if text in line.lower():
                print(line.strip())
except FileNotFoundError:
    print("File not found")
