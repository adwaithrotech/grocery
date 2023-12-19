# Grocery Store Inventory System

# Initialize an empty list to store products
inventory = []

def add_product(name, price, quantity):
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    print(f"{name} added to inventory.")

def display_products():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Products in Inventory:")
        for product in inventory:
            print(f"Name: {product['name']}, Price: ${product['price']}, Quantity: {product['quantity']}")

def search_product(product_name):
    for product in inventory:
        if product['name'] == product_name:
            print(f"Details for {product_name}: Price - ${product['price']}, Quantity - {product['quantity']}")
            return
    print(f"{product_name} not found in inventory.")

def update_quantity(product_name, new_quantity):
    for product in inventory:
        if product['name'] == product_name:
            product['quantity'] = new_quantity
            print(f"Quantity for {product_name} updated to {new_quantity}.")
            return
    print(f"{product_name} not found in inventory.")

def remove_product(product_name):
    for product in inventory:
        if product['name'] == product_name:
            inventory.remove(product)
            print(f"{product_name} removed from inventory.")
            return
    print(f"{product_name} not found in inventory.")

# Main program loop
while True:
    print("\nGrocery Store Inventory System")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Search for a Product")
    print("4. Update Product Quantity")
    print("5. Remove Product")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        name = input("Enter product name: ")
        price = float(input("Enter product price: $"))
        quantity = int(input("Enter product quantity: "))
        add_product(name, price, quantity)

    elif choice == '2':
        display_products()

    elif choice == '3':
        product_name = input("Enter the product name to search: ")
        search_product(product_name)

    elif choice == '4':
        product_name = input("Enter the product name to update quantity: ")
        new_quantity = int(input("Enter the new quantity: "))
        update_quantity(product_name, new_quantity)

    elif choice == '5':
        product_name = input("Enter the product name to remove: ")
        remove_product(product_name)

    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
