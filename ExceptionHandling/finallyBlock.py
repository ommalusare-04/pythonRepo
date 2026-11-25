try:
    f = open("student.txt", "r")
    data = f.read()
    print(data)

except FileNotFoundError:
    print("File not found!")

finally:
    print("File operation completed.")