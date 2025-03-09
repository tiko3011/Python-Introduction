# def happy_birthday(name):
#     print(f"Happy birthday {name}!")
#     print("You are old")
#
#
# happy_birthday("Tiko")

# import datetime
#
#
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due {due_date}")
#
#
# display_invoice("thuggin", 23, datetime.date(2025, 3, 11))

# def add(x, y):
#     z = x + y
#     return z
#
#
# print(add(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("tigran", "Gayranyan")
print(full_name)