# Print names that contain the letter "a". 
f = open("students.txt", "r")

for data in f:
    data = data.replace("\n", "")

    if "a" in data:
        print(data)

f.close()