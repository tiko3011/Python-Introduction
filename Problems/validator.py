username = input("Enter a username: ")

length = len(username)
numOfSpaces = username.count(" ")
noDigit = username.isalpha()
isApproved = length <= 12 and noDigit and not numOfSpaces

decision = "Approved" if isApproved else "Not Approved"
print(decision)
