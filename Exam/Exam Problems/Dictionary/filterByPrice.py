# More than 1000
products = {"laptop": 1500, "mouse": 200, "keyboard": 800, "monitor": 1200}
filteredProducts = {}

items = products.items()

for key, value in items:
    if value > 1000:
        filteredProducts.update({key: value})

print(filteredProducts)