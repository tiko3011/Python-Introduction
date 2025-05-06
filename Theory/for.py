creditCard = "4318-2900-1028-4988"

# for i in range(1, len(creditCard), 1)

# for i in reversed(creditCard):
#     print(i)


for i in creditCard:
    if not i.isdigit():
        continue
    else:
        print(i, end='')