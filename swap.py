
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print(f"Before swap: a = {a} b = {b}")
a = a + b
b = a - b
a = a - b
print("After swap: a = ",a," b = ",b)