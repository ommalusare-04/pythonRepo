while True:
    ope=input("any operator from + - * / ! :")

    if ope=="exit":
        break

    elif ope=="!":
        num=int(input("enter the number :"))
        fact=1
        for i in range(1,num+1):
            fact*=i
        print(f"factorial is {fact}")

    else:
        num1=int(input("enter the number :"))
        num2=int(input("enter the number :"))
        if ope=="+":
            print(f"addition of {num1} and {num2} = {num1+num2}")
        elif ope=="-":
            print(f"substraction of {num1} and {num2} = {num1-num2}")
        elif ope=="*":
            print(f"Multiplication of {num1} and {num2} = {num1*num2}")
        elif ope=="/":
            print(f"Dividation of {num1} and {num2} = {num1/num2}")
        else:
            print("something went wrong try again")
