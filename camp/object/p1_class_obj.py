class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

# 不同的内存地址，两个不同的对象
print(type(a))
print(type(b))
print(id(a))
print(id(b))
print(a.__class__())
print(b.__class__())

# 类也是对象
c = MyFirstClass
d = c()
print(d.__class__())
