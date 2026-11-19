# Save the filtered names (longer than 5 characters) into a new file.

f = open("students.txt","r")
f2 =open("filtered.txt","w")

name=f.readline()
for name in f:
    name=name.replace("\n","")
    if len(name)> 5:
        f2.write(name+"\n")