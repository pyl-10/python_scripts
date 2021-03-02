# 不加进程锁
import time
import multiprocessing as mp

def job(v, num):
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value, end="|")

def multicore():
    v = mp.Value("i", 0) # 定义共享变量
    p1 = mp.Process(target=job, args=(v, 1))
    p2 = mp.Process(target=job, args=(v, 3))  # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    multicore()
