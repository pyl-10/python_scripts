# 让实例的方法成为类的方法
class Kls1(object):
    bar = 1
    def foo(self):
        print('in foo')
    # 使用类属性，方法
    @classmethod
    def class_foo(cls):
        print(cls.bar)
        print(cls.__name__)
        cls().foo()

Kls1.class_foo()

###
class Story(object):
    snake = 'python'
    def __init__(self, name) -> None:
        self.name = name
    # 类的方法
    @classmethod
    def get_apple_to_eve(cls):
        return cls.snake

s = Story('anyone')
# get_apple_to_eve 是bound方法，查找顺序是先找s的__dict__是否含有get_apple_to_eve，如果没有，查类story
print(s.get_apple_to_eve)
# 类和实例都可以使用
print(s.get_apple_to_eve())
print(Story.get_apple_to_eve())

class Kls2():
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me = Kls2('wilson', 'yin')
me.print_name()

# 把输入改为 wilson-yin
# 解决方法一： 修改__init__()
# 解决方法二： 增加__new__（）构造函数
# 解决方法三： 增加 提前处理的函数

def pre_name(obj, name):
    fname, lname = name.split('-')
    return obj(fname, lname)

me2 = pre_name(Kls2, 'wilson-yin')
me2.print_name()

#####
class Kls3():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def pre_name(cls, name):
        fname, lname = name.split('-')
        return cls(fname, lname)

    def print_name(self):
        print(f'first name is {self.fname}')
        print(f'last name is {self.lname}')

me3 = Kls3.pre_name('wilson-yin')
me3.print_name()

###############
'''
    类方法用于模拟java定义多个构造函数的情况
    由于python类中只能有一个初始化方法，不能按照不同的情况初始化类
'''
class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print(f'calling {cls}, {value}')
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

Apple.set(100)
Orange.set(200)

org = Orange()
org.set(300)

Apple.print_total()
Orange.print_total()