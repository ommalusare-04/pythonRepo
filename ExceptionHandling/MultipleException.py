try:
    n=int(input("enter the number:"))
    result=100/n

except (ValueError,ZeroDivisionError) as e:
    print("error",e)