# 父类
class People(object):
    def __init__(self, name) -> None:
        self.gene = 'XY'
        # 假设每人都有名字
        self.name = name

    def walk(self):
        print('I can walk')

# 子类
class Man(People):
    def __init__(self, name) -> None:
        # 找到Man的父类People， 把类People的对象转换为类Man的对象
        super().__init__(name)

    def work(self):
        print('work hard')


class Woman(People):
    def __init__(self, name) -> None:
        self.name = name

    def shopping(self):
        print('buy buy buy')


p1 = Man('adam')
p2 = Woman('eve')

# 问题1 gene 有没有被继承
p1.gene

# 问题2 people的父类是谁
# object and type
print('object', object.__class__, object.__bases__)
print('type', type.__class__, type.__bases__)
# types 元类由 type 自身创建，object类由元类type所创建
# type 类继承了 object 类

# 问题3 能否实现多重层级继承 ： 可以

# 问题4 能否实现多个父类同时继承
class Son(Man, Woman):
    pass