# Allow user three attempts to enter the correct password
correct_password = "python123"

attempts = 3

while attempts > 0:
  password = input('Enter your password: ')
  if password == correct_password:
    print("Login successfull!")
    break
  else:
    attempts -= 1
    print(f"wrong password. {attempts} attempts left.")
else:
  print("Too many incorrect attempts. Acess denied.")