try:
    a=int(input("enter the first number:"))
    b=int(input("enter the second number:"))
    c=a/b
    print(c)

# except ZeroDivisionError :
#     print("divide by zero not possible")

# except:
#     print("invalid input")

except ZeroDivisionError as e:
    print("error:",e)

