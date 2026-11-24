try:
    a=int(input("enter the number:"))
    result=100/a

except ZeroDivisionError as e:
    print("error",e)
    
except:
    print("Something went wrong in input")

