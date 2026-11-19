try:
    password=input("enter password:")
    if len(password) < 8:
        #raise keyword is used to manually generate an exception when a specific condition occurs
        raise ValueError("password must contain atleast 8 characters")
    
    print("valid Password")

except ValueError as e:
    print(e)
