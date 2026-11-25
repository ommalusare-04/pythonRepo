import time
def task(name):
    print(f"{name} started")
    time.sleep(3)
    print(f"{name} completed")

task("task1")
task("task2")
