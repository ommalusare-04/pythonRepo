f = open("demo.txt", "r")

print(f.tell())

data=f.read(4)
print(data)
print(f.tell())

f.close()