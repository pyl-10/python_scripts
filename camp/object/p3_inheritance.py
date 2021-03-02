# 父类
class BaseClass(object):
    num_base_calls = 0
    def call_me(self):
        print('calling method on base class')
        self.num_base_calls += 1

# 子类
class leftSubClass(BaseClass):
    num_left_calls = 0
    # def call_me(self):
    #     print('work hard')
    #     self.num_left_calls += 1


class rightSubClass(object):
    num_right_calls = 0
    def call_me(self):
        print('buy buy buy')
        self.num_right_calls += 1

class subClass(leftSubClass, rightSubClass):
    pass

a = subClass()
a.call_me()

# 问题1 gene 有没有被继承

# 问题2 people的父类是谁
# object and type
# print('object', object.__class__, object.__bases__)
# print('type', type.__class__, type.__bases__)
# types 元类由 type 自身创建，object类由元类type所创建
# type 类继承了 object 类

# 问题3 能否实现多重层级继承 ： 可以

# 问题4 能否实现多个父类同时继承
print(subClass.mro())
# [<class '__main__.subClass'>, <class '__main__.leftSubClass'>, <class '__main__.rightSubClass'>, <class '__main__.BaseClass'>, <class 'object'>]
# 广度优先， python3 中 不加 （object） 也是新式类，但为了代码不会误运行在python2下产生意外结果，仍建议增加
# python2  经典类的查找方式是 深度优先, python3 新式类的查找方式是 广度优先

class Klass(object):
    def A(self):
        pass
    def A(self, a, b):
        print(f'{a}, {b}')

inst = Klass()
# 没有实现重载
inst.A()
