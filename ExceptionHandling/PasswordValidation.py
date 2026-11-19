try:
    password=input("enter password:")
    if len(password) < 8:
        raise ValueError("password must contain atleast 8 characters")
    
    print("valid Password")

except ValueError as e:
    print(e)
