import os

os.fork()
print("111111")
# fork函数运行后会产生出一条新的进程，两个进程一起执行导致输出了两行
