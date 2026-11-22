def employee(name, salary=20000, *skills, city, **details):
    print("Name:", name)
    print("Salary:", salary)
    print("Skills:", skills)
    print("City:", city)
    print("Other Details:", details)


employee(
    "Om",
    25000,
    "Python",
    "Java",
    "SQL",
    city="Pune",
    department="IT",
    experience=2
)

# Symbol	    Purpose
# /	            Positional-only arguments before it
# *args	        Collects extra positional arguments
# *	            Makes following parameters keyword-only
# **kwargs	    Collects extra keyword arguments