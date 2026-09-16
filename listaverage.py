n = int(input("enter the number of list values:"))
list=[]
total=0
for i in range(1,n+1):
    li=int(input("enter the list items:"))
    list.append(li)

for i in list:
    total += i

average=total/n
print(list)
print(total)
print(average)