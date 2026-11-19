try:
    a=int(input("enter the number:"))
    sq=a*a
    print(sq)
except ValueError as v:
    print("error:",v)