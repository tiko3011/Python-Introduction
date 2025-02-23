price1 = 3.145055
price2 = 33.93
price3 = 1253298.282

# { :} -> Specify format

print(f"Precision: ${price1:.3f}")
print(f"How many chars: ${price2:10}")
print(f"Fill with 0: ${price2:010}")
print(f"Left justified: ${price2:<10}")
print(f"Center align: ${price1:^10}")
print(f"Positive and Negative: ${price2:+}")
print(f"Thousand Seperator: ${price3:,}")
print(f"Mix: ${price3:,.2f}")

