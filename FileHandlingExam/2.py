f=open("students.txt","r")
name=f.readline()
for name in f:
    name=name.replace("\n","")
    if len(name)>5:
        print(name)
f.close()
