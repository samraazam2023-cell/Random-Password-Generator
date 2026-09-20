import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

try:
    length = int(input("Enter the password length: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

if length < 3:
    print("Password length must be at least 3.")
    exit()

letters = string.ascii_letters
numbers = string.digits
special_characters = "!@#$%^&*"

# Make sure the password contains at least one number
password = random.choice(numbers)

# Make sure the password contains at least one special character
password += random.choice(special_characters)

# Fill the remaining characters
characters = letters + numbers + special_characters

for i in range(length - 2):
    password += random.choice(characters)

# Shuffle the password
password_list = list(password)
random.shuffle(password_list)
password = "".join(password_list)

print("\nYour generated password is:")
print(password)