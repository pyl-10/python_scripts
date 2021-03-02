from multiprocessing.pool import Pool
import time

def f(x):
    return x*x

if __name__ == "__main__":
    with Pool(processes=4) as pool:
        res = pool.apply_async(f, (10, ))
        print(res.get(timeout=1))

        res = pool.apply_async(time.sleep, (10, ))
        print(res.get(timeout=1))