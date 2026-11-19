try:
    n=int(input("enter tne number:"))

except ValueError as kkk:
    print("error:",kkk)

else:
    print(n)