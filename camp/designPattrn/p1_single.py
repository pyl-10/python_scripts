# 装饰器实现单例模式
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class myClass:
    pass

# myClass 实例化时 因装饰器 传入 singleton 里 为 cls ， 然后 以实例化后的对象传入 instances字典对象，以后实例化时，不会再重复创建
# instances['__main__.myClass']
m1 = myClass()
m2 = myClass()
print(id(m1))
print(id(m2))

class SingleTon(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self, *args, **kwds):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls(*args, **kwds)
        return self._instance[self._cls]

@SingleTon
class myClass2:
    pass

# __new__ 与 __init__ 的关系
class Foo(object):
    def __new__(cls, name):
        print('trace __new__')
        return super().__new__(cls)

    def __init__(self, name):
        print('trace __init__')
        super().__init__()
        self.name = name

bar = Foo('test')
bar.name

#相当于在执行下面的操作
bar = Foo.__new__(Foo, 'test')
if isinstance(bar, Foo):
    Foo.__init__(bar, 'test')


# __new__ 方式实现单例模式 单线程版
class singleton2(object):
    __isinstance = False # 默认没有被实例化
    def __new__(cls, *args, **kwargs):
        if cls.__isinstance:
            return cls.__isinstance # 返回实例化对象
        cls.__isinstance = object.__new__(cls) # 实例化
        return cls.__isinstance

# object 定义了一个名为 singleton 的单例，它满足单例的3个需求
# 一 是只能有一个实例
# 二 是它必须自行创建这个实例
# 三 是它必须自行向整个系统提供这个实例
class _singleton(object):
    pass

Singleton = _singleton()
del _singleton
another = Singleton.__class__()  # 没用，绕过

# __new__

#方法1,实现__new__方法
#并在将一个类的实例绑定到类变量_instance上,
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
#如果cls._instance不为None,直接返回cls._instance
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(
                cls, *args, **kargs)
        return cls._instance

if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    assert id(s1) == id(s2)


# 解决并发， 引入带锁版
import threading
class singleton(object):
    objs = {}
    objs_locker = threading.Lock()
    def __new__(cls, *args, **kargs):
        if cls in cls.objs:
            return cls.objs[cls]
        cls.objs_locker.acquire()  # 加锁
        try:
            if cls in cls.objs:  ## double check locking
                return cls.objs[cls]
            cls.objs[cls] = object.__new__(cls)
        finally:
            cls.objs_locker.release()  # 释放锁

## 利用经典的双检查锁机制，确保了在并发场景下 singleton 的正确实现
# but 这还 可能有以下两个问题
# 如果 singleton 的子类 重载了 __new__() 方法， 会覆盖 or 干扰 singleton 类中的 __new__()的执行
# 如果子类 有 __init__()方法，那么每次实例化该 singleton 的时候
# __init__() 都会被调用到， 这显然是不应该的，__init__()只应该在创建实例的时候被调用一次
# 解决方法：
# 通过文档告诉其他程序员，子类化singleton时， 记得调用__new__()方法
# 偷偷替换掉__init__()方法来确保其只调用一次
# 或 ： python 中模块采用的是天然的单例实现方式
# 所有变量都会绑定到模块
# 模块只初始化一次
# import 机制是线程安全的（保证了在并发状态下模块也只有一个实例）
# 当我们想实现一个游戏世界时，只要简单地创建一个 world.py 就可以了

# world.py
import sun
def run():
    while True:
        sun.rise()
        sun.set()

# main.py
import world
world.run()
