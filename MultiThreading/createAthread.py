import threading
def greet():
    print("Hello From Thread")
t1=threading.Thread(target=greet)
t1.start()