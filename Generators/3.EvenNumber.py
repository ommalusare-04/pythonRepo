def evenNumbers(num):
    for i in range(1, num+1):
        if i % 2 == 0:
            yield i

even = evenNumbers(10)
for i in even:
    print(i,end=" ")