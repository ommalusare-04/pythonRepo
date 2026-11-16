f = open("demo.txt", "r")

print(f.read(5))

f.seek(0)

print(f.read())

f.close()