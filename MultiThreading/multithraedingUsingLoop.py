import threading
import time

def display(num):
    print("Thread", num, "started")
    time.sleep(2)
    print("Thread", num, "completed")

threads = []

for i in range(3):
    t = threading.Thread(target=display, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Main program completed")

