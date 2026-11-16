num1=int(input("enter the number to start:"))
num2=int(input("enter the number to start:"))
while num1 <= num2:
    i = 1

    while i <= 10:
        print(f"{num1} x {i} = {num1 * i}")
        i += 1

    print()
    num1 += 1