
# map
def square(x):
    return x ** 2

m = map(square, range(1, 11))
next(m)
list(m)

[square(x) for x in range(10)]
dir(m)

# reduce（f, [x1, x2, x3]） = f(f(x1, x2), x3)
from functools import reduce
def add(x, y):
    return x + y

reduce(add, [1, 2, 3, 4, 5])

# filter
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 3, 4, 5]))
n = filter(is_odd, [1, 2, 3, 4, 5])
list(n)

# 偏函数
def add(x, y):
    return x + y

import functools
add_1 = functools.partial(add, 1)
add_1(1113)

import itertools
g = itertools.count()
next(g)
next(g)
auto_add_1 = functools.partial(next, g)
auto_add_1()