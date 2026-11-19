
while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        ope = input("Select the operation (+, -, /, *): ")

        if ope == "+":
            result = a + b
        elif ope == "-":
            result = a - b
        elif ope == "/":
            result = a / b
        elif ope == "*":
            result = a * b
        
        else:
            print("Invalid operation")
            continue

        print("Result:", result)

    except ZeroDivisionError as e:
        print("error",e)
    except ValueError:
        print("invalid input")

    choice = input("Enter 1 to continue or 0 to exit: ")

    if choice == "0":
        print("Calculator closed!")
        break
