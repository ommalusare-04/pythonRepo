while True:
    try:
        n1=int(input("enter the first number:"))
        n2=int(input("enter the second number:"))
        ope=input("enter the operation like +,-,/,*")

        if ope == "+":
            result=n1+n2
        elif ope == "-":
            result=n1-n2
        elif ope == "/":
            result=n1/n2
        elif ope == "*":
            result=n1*n2
        else:
            print("invalid operation")
            continue

        print("result:",result)

    except (ZeroDivisionError,ValueError) as z:
        print("error:",z)


    choice=int(input("enter 1 to continue 0 to exit:"))
    if choice==0:
        print("Exit calculator")
        break
        