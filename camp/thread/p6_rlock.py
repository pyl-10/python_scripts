import threading
import time

# lock普通锁不可嵌套，rlock普通锁可嵌套
mutex = threading.RLock()

class MyThread(threading.Thread):
    def run(self):
        if mutex.acquire(1):
            print("线程" + self.name + " get mutex")
            time.sleep(1)
            mutex.acquire()
            mutex.release()
        mutex.release()

if __name__ == "__main__":
    for i in range(5):
        t = MyThread()
        t.start()