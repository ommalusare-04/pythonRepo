# Default Arguments
# A parameter has a predefined value. If the user doesn't pass a value, Python uses the default.
def student(name, course="MCA"):
    print("Name:", name)
    print("Course:", course)

student("Om")
student("Rahul", "MBA")
# Logic: If no course is provided, the default "MCA" is used.
