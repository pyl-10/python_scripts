# import queue
# q = queue.Queue(5)
# q.put(111)   # 存队列
# q.put(222)
# q.put(233)

# print(q.get())  # 取队列
# print(q.get())
# q.task_done()  # 每次从队列中get一个数之后，当处理好相关问题，最后调用该方法
#                 # 以提示 q.join() 是否停止阻塞，让线程继续执行或退出
# print(q.qsize())  # 队列中元素的个数， 队列的大小
# print(q.empty())  # 队列是否为空
# print(q.full())  # 队列是否满了

##################

import queue
import threading
import random
import time

writelock = threading.Lock()  # 写入锁

class Producer(threading.Thread):
    def __init__(self, q, con, name):
        super(Producer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print(f"producer {self.name} started")

    def run(self):
        while 1:
            global writelock
            self.con.acquire() # 获得锁对象

            if self.q.full():  # 如果队列是满的
                with writelock:
                    print("队列已满，请等待生产")
                self.con.wait()  # 等待资源
            else:
                value = random.randint(0, 10)
                with writelock:
                    print(f"{self.name} put value {self.name} {str(value)} in queue")
                self.q.put((f"{self.name}: {str(value)}")) # 放入队列
                self.con.notify()  # 通知消费者
                time.sleep(1)
        self.con.release()


class Consumer(threading.Thread):
    def __init__(self, q, con, name):
        super(Consumer, self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print(f"consumer {self.name} started")

    def run(self):
        while 1:
            global writelock
            self.con.acquire()
            if self.q.empty():   # 队列为空
                with writelock:
                    print("队列为空，消费者请等待")
                self.con.wait()  # 等待资源
            else:
                value = self.q.get()
                with writelock:
                    print(f"{self.name} get value {value} from queue")
                self.con.notify()  # 通知生产者
                time.sleep(1)
        self.con.release()

if __name__ == "__main__":
    q = queue.Queue(10)
    con = threading.Condition()  # 条件变量锁

    p1 = Producer(q, con, "p1")
    p1.start()
    p2 = Producer(q, con, "p2")
    p2.start()
    p3 = Consumer(q, con, "p3")
    p3.start()

# 练习使用列表实现队列

