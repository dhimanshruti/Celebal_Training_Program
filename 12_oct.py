products = ["laptop","smartphone","tablet","telephones"]
products.append("monitor") #add a new product
products[0] = "gaming laptop"
products.remove("tablet")
print(products)

print("watch in products")

product = ("P1","Keyboard",3500)
product_id, name, price = product



# Dictionaries of product details
inventory = {
    "P1": {"name": "keyboard", "price": 3500, "quantity": 50},
    "P2": {"name": "Mouse", "price": 1500, "quantity": 100},
    "P3": {"name": "Monitor", "price": 1200, "quantity": 30}
}

print(inventory)
print(inventory.keys())
print(inventory.values())

online_customers = {"Alice","Bob","Charlie","David"}
returning_customers = {"Bob", "Eve","Frank","Charlie"}
print(online_customers | returning_customers)
print(online_customers & returning_customers)
print(online_customers - returning_customers)

