# 加进程锁
# 为了解决不同进程抢共享资源的问题，我们可以用加进程锁来解决。
import multiprocessing as mp
import time

# 在 job()中设置进程锁的使用，保证运行时一个进程的对锁内内容的独占
def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1)
        v.value += num # 获取共享内存
        print(v.value, end="|")
    l.release()  # 释放


def multicore():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value("i", 0) # 定义共享内存
    # 进程锁的信息给入各个进程中
    p1 = mp.Process(target=job, args=(v, 1, l))
    p2 = mp.Process(target=job, args=(v, 3, l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == "__main__":
    multicore()
