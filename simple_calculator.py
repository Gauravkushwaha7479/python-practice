import sys 
sys.set_int_max_str_digits(1000000)


while True:
    try:

        num1 = int(input("Enter the first number\n"))
        num2 = int(input("Enter the second number\n"))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        continue

    
    operator = input("Enter the operator\n")

    if operator == "+":
        print(f"{num1} + {num2} = {num1+num2}")

    elif operator == "-":
        print(f"{num1} - {num2} = {num1-num2}")

    elif operator == "*":
        print(f"{num1} * {num2} = {num1*num2}")

    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"{num1} / {num2} = {num1/num2}")

    elif operator == "%":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")

        else:
            print(f"{num1} % {num2} = {num1%num2}")

    elif operator == "**":
        print(f"{num1} ** {num2} = {num1**num2}")


    else:
        print("Invalid operator. Please use one of the following: +, -, *, /, %, **")