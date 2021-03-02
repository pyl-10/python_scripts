# line() 的定义引用了 外部的变量
def line_conf():
    b = 10
    def line(x):
        return 2*x+b
    return line

b = -1
my_line = line_conf()
print(my_line(5))

# 编译后函数体保存的局部变量
print(my_line.__code__.co_varnames)
# 编译后函数体保存的自由变量
print(my_line.__code__.co_freevars)
# 自由变量真正的值
print(my_line.__closure__[0].cell_contents)

# 函数和对象比较有哪些不同的属性
# 函数还有哪些属性
def func():
    pass
func_magic = dir(func)

# 常规对象有哪些属性
class ClassA():
    pass
obj = ClassA()
obj_magic = dir(obj)

# 比较函数和对象的默认属性
set(func_magic) - set(obj_magic)

# 进化版
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print(line1(5), line2(5))

# 内部函数对外部函数作用域里变量的引用（非全局变量） 则称为内部函数的闭包
def counter(start=0):
    count=[start]
    def incr():
        count[0]+=1
        return count[0]
    return incr

c1=counter(10)
print(c1())
print(c1())
print(c1())

# nonlocal 访问外部函数的局部变量
# 注意 start 的位置， return 的作用域和函数内的作用域不同
def counter2(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr

c1 = counter2(5)
print(c1())
print(c1())

c2 = counter2(50)
print(c2())
print(c2())