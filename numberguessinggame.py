#Create a game where the user has to guess a random number between 1 and 100. Provide hints like "Too High" or "Too Low" and limit the number of guesses.
## Generate a random number between 1 and 100
import random

target_number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number (between 1 and 100):")


while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess == target_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < target_number:
        print("Too low!")
    else:
        print("Too high!")

if attempts == max_attempts and guess != target_number:
    print(f"Sorry, you've used all your attempts. The number was {target_number}.")