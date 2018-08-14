""" Chloe Harrison """

MIN_LENGTH = 5

password = input("Enter password: ")

while len(password) < MIN_LENGTH:
    print("Needs 5 characters")
    password = input("Enter password: ")

print("*" * len(password))
