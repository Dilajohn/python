# Variables
name = "Alice"  # string
age = 25  # int
Height = 5.6  # float
is_student = True  # boolean

# collection
# (List): [1, 2, 3]
# (Tupple):(1, 2, 3)
# set : {1,2,3}
# dictionary :{"key": "value"}

print(type(name))
print(type(age))

# convert types

age = int("25")  # string to integer
Height = float("5.6")  # str to float

print(age)
print(Height)

print("Hello, world!")
name = "Alice"
print("My name is", name)

# input
# Use input() to get user input. It always returns a string.
name = input("Enter your name: ")
print("Hello,", name)

# Convert input to other types if needed
age = int(input("Enter your age: "))  # Converts input to integer

#### Basic Operators
# Arithmetic Operators(Perform mathematical operations)
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.3333...
print(a // b)  # Floor Division: 3
print(a % b)  # Modulus: 1 (remainder)
print(a**b)  # Exponentiation: 1000

# Comparison Operators(Compare values, return True or False)
print(a > b)  # Greater than: True
print(a < b)  # Less than: False
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# Logical Operators(Combine multiple conditions)
x = True
y = False
print(x and y)  # Logical AND: False
print(x or y)  # Logical OR: True
print(not x)  # Logical NOT: False

# Examples: Combining These Concepts
# Example 1: User Input with Arithmetic
# Get user input and calculate sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The sum is:", num1 + num2)

# Example 2: Logical and Comparison Operations
num = 15
if num > 10 and num < 20:
    print("Number is between  10 and 20")
else:
    print("Number is outside the range")
