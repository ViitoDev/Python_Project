try:
    num1 = int(input("Enter the first number: \n"))
    num2 = int(input("Enter the second number: \n"))
    operation = str(input("Choose a operation: + | - | * | /\n"))
    if operation == "+":
        print("The result is:\n", num1 + num2)
    elif operation == "-":
        print("The result is:\n", num1 - num2)
    elif operation == "*":
        print("The result is:\n", num1 * num2)
    elif operation == "/":
        print("The result is:\n", num1 / num2)
except ValueError:
    print("Invalid character.")
except ZeroDivisionError:
    print("Invalid operation, division per zero.")