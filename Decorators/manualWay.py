def greet(name):
    return f"hello {name}"

def my_deocrator(func):
    def wrapper():
        print("before Function runs")
        result=func("om")
        print(result)
        print("after function runs")
    return wrapper

decorated=my_deocrator(greet)
decorated()