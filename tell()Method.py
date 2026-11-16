f = open("demo.txt", "r")

print(f.tell())

data = f.read()
print(data)

print(f.tell())

f.close()