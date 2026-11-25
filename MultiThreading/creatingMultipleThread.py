import threading

def student1():
    print("Student 1 is studying")

def student2():
    print("Student 2 is writing")

t1 = threading.Thread(target=student1)
t2 = threading.Thread(target=student2)

t1.start()
t2.start()