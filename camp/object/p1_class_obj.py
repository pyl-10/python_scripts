class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

# 不同的内存地址，两个不同的对象
type(a)
type(b)
id(a)
id(b)
a.__class__()
b.__class__()

# 类也是对象
c = MyFirstClass
d = c()
d.__class__()
