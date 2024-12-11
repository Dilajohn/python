#Control Flow in Python
#Control flow statements allow you to control the execution of code based on conditions or iterations.
#1. If-else Statements
#if condition:
    # Code to execute if the condition is True
#elif another_condition:
    # Code to execute if another_condition is True
#else:
    # Code to execute if all conditions are False
#

age = 20

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")


#2 Loops
#For Loop(Used to iterate over a sequence (like a list, string, or range).)
#SYNTAX
#(for item in sequence:
    # Code to execute for each item
#) 

#ex 1:Iterating over a list:
fruits = ["apple", "banana","cherry"]
for fruit in fruits:
    print(fruit)

#  Using range():
for i in range(5):  # Iterates from 0 to 4
    print(i)

#:While Loop(Used to repeat a block of code as long as a condition is True.)
#SYNTTAX
#while condition:
    # Code to execute while condition is True
#ex:
count = 5
while count > 0:
    print(count)
    count -= 1

#3. Break, Continue, and Pass
#Break(Exits the loop immediately.)
for num in range(10):
    if num == 5:
        break  # Stops the loop when num is 5
    print(num)

#Continue(Skips the rest of the loop's body for the current iteration and moves to the next iteration.)
for num in range(5):
    if num == 2:
        continue  # Skips the rest of the code for num = 2
    print(num)

#Pass(Does nothing; a placeholder for code that will be added later.)
for num in range(5):
    if num == 2:
        pass  # Placeholder, no action taken
    print(num)


#PUTTING IT ALL TOGETHER
#EX1:Even and Odd Numbers with Control Flow
for num in range(1, 10):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#Example: Using While with Break
count = 0
while count < 10:
    if count == 5:
        break  # Exit the loop when count reaches 5
    print(count)
    count += 1
