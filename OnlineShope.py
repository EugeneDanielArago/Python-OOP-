class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity}"


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product):
        
        for item in self.cart:
            if item.name.lower() == product.name.lower():
                item.quantity += product.quantity
                print(f"Updated '{item.name}' quantity to {item.quantity}")
                return
        
        self.cart.append(product)
        print(f"'{product.name}' added to the cart.")

    def remove_product(self, product_name):
        for item in self.cart:
            if item.name.lower() == product_name.lower():
                self.cart.remove(item)
                print(f"'{product_name}' removed from the cart.")
                return
        print(f"Product '{product_name}' not found in the cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\n--- Your Cart ---")
            for product in self.cart:
                print(product)

    def calculate_total(self):
        total = sum(product.price * product.quantity for product in self.cart)
        return total

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Nothing to checkout.")
        else:
            total = self.calculate_total()
            print("\n--- Checkout Summary ---")
            self.view_cart()
            print(f"Total Price: ${total:.2f}")
            print("Thank you for your purchase!")

cart = ShoppingCart()

while True:
    print("\n--- Online Shopping Cart Menu ---")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Calculate Total Price")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        name = input("Enter product name: ")
        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(name, price, quantity)
            cart.add_product(product)
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")

    elif choice == 2:
        name = input("Enter product name to remove: ")
        cart.remove_product(name)

    elif choice == 3:
        cart.view_cart()

    elif choice == 4:
        total = cart.calculate_total()
        print(f"\nTotal price: ${total:.2f}")

    elif choice == 5:
        cart.checkout()

    elif choice == 6:
        print("Exiting shopping cart. Goodbye!")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")
