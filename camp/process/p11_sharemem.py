# 可以使用 Value or Array 将数据存储在共享内存映射中
# 这里的 Array 和 numpy 中的不同， 它只能是一维的，不能是多维的
# 同样和 Value 一样，需要定义数据形式， 否则会报错

from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in a:
        a[i] = -a[i]

if __name__ == "__main__":
    num = Value("d", 0.0)
    arr = Array("i", range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])