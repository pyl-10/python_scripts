from multiprocessing import Process, Pipe
def f(conn):
    conn.send([42, None, "hello"])
    conn.close()

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn, ))
    p.start()
    print(parent_conn.recv())
    p.join()

# 返回两个连接对象 Pipe() 表示管道的两头
# 每个连接对象都有 send() 和 recv() 方法 (相互之间的)
# 请注意， 如果两个进程 (或线程) 同时尝试读取或写入管道的 同一端
# 则管道中的数据可能会损坏， 当然， 同时使用管道的不同端的进程不存在损坏的风险