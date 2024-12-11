#Functions are reusable blocks of code designed to perform specific tasks. They help in reducing code redundancy, improving readability, and making programs more modular.
#
# 1. Defining and Calling Functions
#Defining a Function(Use the def keyword followed by the function name and parentheses.)
#Syntax
#def function_name():
    # Code block
#    pass

#Calling a Function
#Invoke the function by using its name followed by parentheses.

def greet():
    print("Hello, World!")

# Call the function
greet()

#2. Arguments and Return Values

#Arguments
#Functions can accept input values called arguments, which are specified in the parentheses.
#Example: Function with Arguments

def greet(name):
    print(f"Hello, {name}!")

greet("DILA")  # Output: Hello, DILA!

#Return Values
#Functions can return values using the return keyword.
#Example: Function with Return Value
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"The sum is: {result}")  # Output: The sum is: 8


#3. Default Arguments
# Default arguments allow you to provide a default value for a parameter. If the argument is not provided during the function call, the default value is used.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("DILA")  # Output: Hello, DILA!

#4. Keyword Arguments
#When calling a function, you can use keyword arguments to specify parameters explicitly, regardless of their order.
def display_info(name, age):
    print(f"Name: {name}, Age: {age}")

display_info(age=30, name="Bob")  # Output: Name: Bob, Age: 30


#Combining All Concepts
#Function with Default and Keyword Arguments
def calculate_total(price, tax=0.05, discount=0):
    """
    Calculate the total price after tax and discount.
    """
    total = price + (price * tax) - discount
    return total

# Using default tax and specifying discount
total_price = calculate_total(100, discount=10)
print(f"Total price: {total_price}")  # Output: Total price: 95.0

# Specifying tax and discount
total_price = calculate_total(100, tax=0.08, discount=5)
print(f"Total price: {total_price}")  # Output: Total price: 103.0


#Best Practices for Functions

#Write Descriptive Function Names: Names should clearly indicate the function’s purpose.
def calculate_area(radius):
    pass

#Use Docstrings: Document the purpose of the function and its parameters.
def greet(name):
    """Greets the user by their name."""
    print(f"Hello, {name}!")

#Keep Functions Short: Functions should do one thing and do it well.

#Return Instead of Print: Functions should typically return results for flexibility.
def square(num):
    return num ** 2


