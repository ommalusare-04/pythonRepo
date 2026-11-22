def student(name, age, /, course="MCA", *, city):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)

student("Om", 22, "MBA", city="Pune")