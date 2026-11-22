def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("before function runs")
        result=func(*args,**kwargs)
        print(result)
        print("After function runs")
    return wrapper
    
@my_decorator
def greet(name,rollno):
    return f"Name: {name}\nRoll Number:{rollno}"

greet("om",rollno=21)