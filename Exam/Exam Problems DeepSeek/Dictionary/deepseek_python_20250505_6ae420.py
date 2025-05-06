products = {"laptop": 1500, "mouse": 200, "keyboard": 800, "monitor": 1200}
filtered = {k:v for k,v in products.items() if v > 1000}
print("Filtered products:", filtered)