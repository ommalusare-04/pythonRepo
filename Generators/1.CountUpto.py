def count_upto(num):
    i=1
    while i <= num:
        yield i
        i+=1
value=count_upto(5)
print(next(value))  #1
for val in value:
    print(val) #2,3,4,5