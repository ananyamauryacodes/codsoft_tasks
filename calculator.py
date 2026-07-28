print("=" * 40)
print("       BASIC CALCULATOR")
print("=" * 40)

while True:
    first_num = float(input("Enter the first number: "))
    second_num = float(input("Enter the second number: "))
    operator = input("Choose an operator (+, -, *, /): ")

    if operator == "+":
        print("Result =", first_num + second_num)

    elif operator == "-":
        print("Result =", first_num - second_num)

    elif operator == "*":
        print("Result =", first_num * second_num)

    elif operator == "/":
        if second_num == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result =", first_num / second_num)

    else:
        print("Please enter a valid operator.")

    choice = input("Would you like to perform another calculation? (yes/no): ").lower()

    if choice == "no":
        print("Thanks for using this calculator. Have a great day!")
        break
