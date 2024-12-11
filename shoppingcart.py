#Create a function to calculate the total price of items in a shopping cart. The function should handle optional tax and discount values.
def calculate_total(cart_items, tax=0.05, discount=0):
    """
    Calculate the total price of items in a shopping cart.
    
    Args:
        cart_items (list of float): List of item prices.
        tax (float): Tax rate to apply. Default is 5% (0.05).
        discount (float): Discount to subtract. Default is 0.
    
    Returns:
        float: The total price after tax and discount.
    """
    subtotal = sum(cart_items)
    total = subtotal + (subtotal * tax) - discount
    return total

# Example cart
cart = [100, 50, 25]  # Item prices

# Test the function
print("Cart Total (No discount):", calculate_total(cart))  # Output: 183.75
print("Cart Total (With discount):", calculate_total(cart, discount=20))  # Output: 163.75
print("Cart Total (Custom tax):", calculate_total(cart, tax=0.1))  # Output: 192.5
