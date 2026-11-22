# Variable-Length Keyword Arguments (**kwargs)
# Used when we don't know how many keyword arguments will be passed.

# Example 1
def student(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    # print(kwargs)
student(name="Om",age=21,course="MCA")


# example 2 
# def employee(**details):
#     for key, value in details.items():
#         print(key, ":", value)

# employee(
#     name="Om",
#     salary=25000,
#     department="IT",
#     experience=2
# )