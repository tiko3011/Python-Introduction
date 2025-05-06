import os

# file_path = "Test.txt"

# if os.path.exists(file_path):
#     if os.path.isfile(file_path):
#         print("This is a file")
#     else:
#         print("This is a folder")
# else:
#     print("Nah")

# file_path = "output.txt"
#
# txt_data = "Some random text that has " \
#            "so much meaning y'all cant understand"
# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"Text file {file_path} is created")

file_path = "Test.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
