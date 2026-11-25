try:
    n=int(input("enter the number:"))
    result=100/n
    

except (ValueError,ZeroDivisionError,TypeError) as e:  # exception object
    print("error",e)

else:
    print(result)