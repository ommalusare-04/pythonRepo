

f=open("students.txt","r")

count=0
for data in f:
    data=data.lower()
    if data.startswith(("a","e","i","o","u")):
        count+=1
print(count)