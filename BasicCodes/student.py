role = input("Enter role: ")
age = int(input("Enter age: "))
print(f"Eligible: {role == 'student' and age < 21}")