# -----------------------------------------
# Password Generator
# Generates a random password based on the
# length entered by the user.
# -----------------------------------------

import random
import string

while True:

    print("======================================")
    print("       PASSWORD GENERATOR")
    print("======================================")

    password_chars = string.ascii_letters + string.digits

    password_length = int(input("Enter password length: "))

    if password_length <= 0:
        print("Invalid password length!")

    else:

        symbol_option = input("Include special characters? (yes/no): ").strip().lower()

        if symbol_option == "yes":
            password_chars += string.punctuation

        print("Generated Password: ", end="")

        for i in range(password_length):
            print(random.choice(password_chars), end="")

        print()

        choice = input("Generate another password? (yes/no): ").strip().lower()

        if choice == "no":
            print("Thank you for using the Password Generator!")
            break

        elif choice == "yes":
            continue

        else:
            print("Invalid choice! Please enter 'yes' or 'no'.")
