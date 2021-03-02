import threading
import time

num = 0

def add():
    global num
    num += 1
    time.sleep(1)
    print(f"num value is {num}")

for i in range(10):
    t = threading.Thread(target=add)
    t.start()

print("主线程停止")