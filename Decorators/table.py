def my_decorator(func):
    def wrapper(*args):
        print("before function runs")
        result=func(*args)
        print(result)
        print("After function runs")
    return wrapper
    
@my_decorator
def table(num):
    for i in range(1,11):
        print(num*i)

table(8)