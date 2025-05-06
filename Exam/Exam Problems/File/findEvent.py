file_path = "txt/events.txt"
text = "2025-04-15"

try:
    with open(file_path, "r") as file:
        for line in file:
            if text in line:
                print(line.strip())
except FileNotFoundError:
    print("File not found")