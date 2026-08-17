import string
import random

chars = list(string.ascii_letters + string.digits+ "!@#$%^&*")

def generate_password():
    password_len = int(input("How long you want your password to be: "))

    random.shuffle(chars)
    password = []

    for i in range(password_len):
        password.append(random.choice(chars))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password(Y/N):").lower()

if option == "y":
    generate_password()
elif option == "n":
    print("End....")
else:
    print("Invalid input only(Y/N)")