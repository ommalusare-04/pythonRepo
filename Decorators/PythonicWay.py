def my_decorator(func):
    def wrapper(*args):
        print("before function runs")
        result=func(*args)
        print(result)
        print("After function runs")
    return wrapper
    
@my_decorator
def greet(name):
    return f"Hello {name}"

greet("om")