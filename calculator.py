from functions import calculate_total
from palindromechecker import is_palindrome
from simplecalculator import calculator


def main():
    print("Welcome to the Interactive Calculator!")
    while True:
        print("\nMenu:")
        print("1. Simple Calculator")
        print("2. Palindrome Checker")
        print("3. Shopping Cart Total")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            # Simple Calculator
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            result = calculator(num1, num2, operator)
            print(f"Result: {result}")
        
        elif choice == "2":
            # Palindrome Checker
            string = input("Enter a string to check: ")
            if is_palindrome(string):
                print(f"'{string}' is a palindrome.")
            else:
                print(f"'{string}' is not a palindrome.")
        
        elif choice == "3":
            # Shopping Cart Total
            cart_size = int(input("Enter the number of items in your cart: "))
            cart = []
            for i in range(cart_size):
                price = float(input(f"Enter price of item {i + 1}: "))
                cart.append(price)
            tax = float(input("Enter tax rate (default 0.05): ") or 0.05)
            discount = float(input("Enter discount (default 0): ") or 0)
            total = calculate_total(cart, tax, discount)
            print(f"Total Cart Price: {total}")
        
        elif choice == "4":
            print("Thank you for using the calculator. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Call the main function
main()
