n=int(input("enter the number:"))
freq=[0]*10
while n > 0:
    ld=n%10
    freq[ld]+=1
    n=n//10

for i in range(10):
    if freq[i] == 0:
        print(f"{i}=0")
    else:
        print(f"{i}={freq[i]}")
