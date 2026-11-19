
try:
    rollno=int(input("enter the roll no:"))
    name=input("enter the name:")
    marks=float(input("enter the marks"))
    if marks <= 100 and marks > 0:
        if marks >=75:
            grade = "A"
        elif marks >=60:
            grade = "B"
        elif marks >=40:
            grade = "C"
        else:
            grade = "F"
    else:
        print("invalid marks")
except ValueError as v:
    print("error:",v)

else:
    print(f"Roll Number:{rollno}")
    print(f"Name : {name}")
    print(f"Marks : {marks}")
    print(f"Grades : {grade}")

        