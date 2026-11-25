import threading
def student(name):
    print(f"name: {name}")

t1=threading.Thread(target=student,args=("om",))
t2=threading.Thread(target=student,args=("rahul",))

t1.start()
t2.start()

t1.join()
t2.join()