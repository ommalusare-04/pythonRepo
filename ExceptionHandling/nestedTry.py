try:
    num=int(input("enter the number:"))
    try:
        result=100/num
        print(result)
    except (ValueError,ZeroDivisionError) as e:
        print("error",e)
        
finally:
    print("code executed")