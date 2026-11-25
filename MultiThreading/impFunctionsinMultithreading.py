import threading

def task():
    print("Task running")

t1 = threading.Thread(target=task)

t1.start()

print(t1.is_alive())

t1.join()

print(t1.is_alive())