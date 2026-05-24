import re

# Take password input
password = input("Enter your password: ")

# Conditions
length = len(password) >= 8
number = re.search(r"\d", password)
uppercase = re.search(r"[A-Z]", password)
special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

# Check password strength
if length and number and uppercase and special:
    print("Strong Password")
else:
    print("Weak Password")