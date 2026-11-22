# Keyword-Only Arguments
# Parameters after * must be passed using their names.
def employee(name,age, *,company):
    print(f"name:{name}")
    print(f"age:{age}")
    print(f"company:{company}")

employee("sagar",33,company="Google")