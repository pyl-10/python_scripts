# 现在有这样一个需求：我们有两个进程，一个进程负责写，一个进程负责读
# 当写的进程写完某部分以后要把数据交给读的进程进行使用
# write()将写完的数据交给队列，再有队列交给read()

from multiprocessing import Process, Queue

def f(q):
    q.put([42, None, "hello"])

if __name__ == "__main__":
    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    print(q.get())
    p.join()

# 队列是线程和进程安全的