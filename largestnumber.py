# Find the largest number in a list
numbers = [34, 78, 23, 56, 90, 12]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}.")