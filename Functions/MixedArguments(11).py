# Mixed Arguments
# Python allows us to combine different argument types.

def student(name,*marks,**details):
    print(f"name:{name}")
    print(f"marks:{marks}")
    print(f"Details:{details}")


student("om",56,78,65,city="Satara",course="MCA")