products = {"laptop": 1500, "mouse": 200, "keyboard": 800, "monitor": 1200}

# Filter expensive products
expensive = {}
for name, price in products.items():
    if price > 1000:
        expensive[name] = price

print("Expensive products:", expensive)