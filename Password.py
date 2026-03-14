import re

print("Password Strength Checker")

password = input("Enter your password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if re.search("[A-Z]", password):
    strength += 1

if re.search("[0-9]", password):
    strength += 1

if re.search("[@#$%^&*!]", password):
    strength += 1

if strength <= 1:
    print("Weak Password")

elif strength == 2 or strength == 3:
    print("Medium Password")

else:
    print("Strong Password")
