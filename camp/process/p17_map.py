from multiprocessing.pool import Pool
import time

def f(x):
    return x*x

if __name__ == "__main__":
    with  Pool(processes=4) as pool:
        print(pool.map(f, range(10)))  # map 返回的是一个列表

        it = pool.imap(f, range(10))  # imap 返回的是一个迭代器
        print(it)
        print(next(it))
        print(next(it))
        print(it.next(timeout=1))