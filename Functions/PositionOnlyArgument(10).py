# Positional-Only Arguments
# Parameters before / must be passed positionally.
def student(name, age, /,course):
    print(name, age,course)

student("Om", 22,course="MCA")

