#Create a program that simulates an ATM system. Users can log in with a PIN, check their balance, deposit money, and withdraw money. Use control flow to manage operations and exit conditions.

#Features
#Validate the user's PIN.
#Display menu options (e.g., Check Balance, Deposit, Withdraw, Exit).
#Handle invalid input gracefully.
#Use break to exit the system.

balance = 1000  # Initial balance
pin = "1234"    # Set a PIN
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ")
    if entered_pin == pin:
        print("Login successful!")
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                print(f"Your balance is ${balance}.")
            elif choice == "2":
                deposit = float(input("Enter amount to deposit: "))
                balance += deposit
                print(f"${deposit} deposited. New balance: ${balance}.")
            elif choice == "3":
                withdraw = float(input("Enter amount to withdraw: "))
                if withdraw > balance:
                    print("Insufficient balance.")
                else:
                    balance -= withdraw
                    print(f"${withdraw} withdrawn. New balance: ${balance}.")
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. {attempts} attempts left.")
else:
    print("Too many incorrect attempts. Access locked.")
