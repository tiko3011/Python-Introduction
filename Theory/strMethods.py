name = "Tigran Gayranyan"

length = len(name)
firstOne = name.find(" ")
lastOne = name.rfind(" ")
name = name.capitalize()

print(f"Full name length -> {length}")  # Length of Full Name
print(f"First space index -> {firstOne}")  # Length of First Name
print(f"Last space index -> {lastOne}")
print(f"Number of A -> {name.count('A')}")
print(f"Spaces replaced -> {name.replace(' ', '-')}")
print(f"If il n'y a pas symbol -> {name.find('#')}")  # -1
print(f"Is Digit? -> {name.isdigit()}")
print(f"IsAlpha (Alphabetical Char) -> {name.isalpha()}")

name = name.upper()
print(f"Capitalized -> {name}")

name = name.lower()
print(f"DeCapitalized -> {name}")

