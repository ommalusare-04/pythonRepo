import threading
import time

def task1():
    print("task 1 started")
    time.sleep(4)
    print("task 1 completed")

def task2():
    print("task 2 started")
    time.sleep(4)
    print("task 2 completed")

t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)

t1.start()
t2.start()

# join() makes the main thread wait until the specified thread finishes.
# Without join(), the main thread may continue executing before these tasks complete.
t1.join()
t2.join()

print("tasks completed successfully")