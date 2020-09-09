first_number = float(input("Enter number here: "))

second_number = float(input("Enter a second number here: "))

operand = input("Choose an operand: +, -, *, / ")

if operand == "+":
    print(first_number + second_number)

elif operand == "-":
    print(first_number - second_number)

elif operand == "*":
    print(first_number * second_number)

elif operand == "/":
    print(first_number / second_number)

elif second_number == "0":
    print("Cannot divide by zero.")
