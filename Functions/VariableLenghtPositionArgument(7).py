# Variable-Length Positional Arguments (*args)
# Used when we don't know how many positional arguments the user will pass.

# Addition of Multiple arguments passed using *args.

# def addition(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(f"addition is:",addition(12,34,6,7,8))


# find maximum number from li using *args.
def max_number(*args):
    if len(args) == 0:
        return
    maximum=args[0]
    for i in args:
        if i > maximum:
            maximum=i
    return maximum

nums=int(input("enter the number of elements needed:"))
li=[]
for i in range(nums):
    num=int(input("enter the number:"))
    li.append(num)
print(li)
print(max_number(*li))