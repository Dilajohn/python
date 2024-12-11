# Extending the Shopping Cart Example

# Adding item names and quantities to the cart.
# Allowing users to add, remove, or update items dynamically.
# Providing a summary of the cart and total price with tax and discount.


def add_item(cart):
    """Add an item to the shopping cart."""
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the quantity: "))
    cart[name] = {"price": price, "quantity": quantity}
    print(f"Added {quantity} x {name} to the cart.")


def remove_item(cart):
    """Remove an item from the shopping cart."""
    name = input("Enter the item name to remove: ")
    if name in cart:
        del cart[name]
        print(f"{name} removed from the cart.")
    else:
        print("Item not found in the cart.")


def update_item(cart):
    """Update the quantity or price of an item in the shopping cart."""
    name = input("Enter the item name to update: ")
    if name in cart:
        price = float(input("Enter the new price: "))
        quantity = int(input("Enter the new quantity: "))
        cart[name] = {"price": price, "quantity": quantity}
        print(f"Updated {name} to {quantity} x {price}.")
    else:
        print("Item not found in the cart.")


def calculate_total(cart, tax=0.05, discount=0):
    """Calculate the total price of items in the cart."""
    subtotal = sum(item["price"] * item["quantity"] for item in cart.values())
    total = subtotal + (subtotal * tax) - discount
    return subtotal, total


def display_cart(cart):
    """Display all items in the shopping cart."""
    if not cart:
        print("Your cart is empty.")
        return
    print("\nShopping Cart:")
    print("{:<15} {:<10} {:<10} {:<10}".format("Item", "Price", "Quantity", "Total"))
    for name, details in cart.items():
        item_total = details["price"] * details["quantity"]
        print(
            f"{name:<15} ${details['price']:<10.2f} {details['quantity']:<10} ${item_total:.2f}"
        )
    print("-" * 50)


def main():
    """Main function to manage the shopping cart."""
    cart = {}
    while True:
        print("\nShopping Cart Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_item(cart)
        elif choice == "2":
            remove_item(cart)
        elif choice == "3":
            update_item(cart)
        elif choice == "4":
            display_cart(cart)
        elif choice == "5":
            if not cart:
                print("Your cart is empty. Add items before checkout.")
            else:
                tax = float(input("Enter tax rate (default 0.05): ") or 0.05)
                discount = float(input("Enter discount (default 0): ") or 0)
                subtotal, total = calculate_total(cart, tax, discount)
                display_cart(cart)
                print(f"\nSubtotal: ${subtotal:.2f}")
                print(f"Tax: ${subtotal * tax:.2f}")
                print(f"Discount: ${discount:.2f}")
                print(f"Total: ${total:.2f}")
                print("Thank you for shopping with us!")
                break
        elif choice == "6":
            print("Thank you! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
main()
