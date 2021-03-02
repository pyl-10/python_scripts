# 静态工厂模式
class Human(object):
    def __init__(self) -> None:
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Man(Human):
    def __init__(self, name):
        print(f'hi, man {name}')

class Woman(Human):
    def __init__(self, name):
        print(f'hi, woman {name}')

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Man(name)
        elif gender == 'F':
            return Woman(name)
        else:
            pass

if __name__ == "__main__":
    factory = Factory()
    person = factory.getPerson('adam', 'M')

# 动态工厂模式 返回在函数内动态创建的类
def factory2(func):
    class klass: pass
    # setattr 需要三个参数 ： 对象， key， value
    # print(func)
    # setattr(klass, func.__name__, func)
    setattr(klass, func.__name__, classmethod(func))
    return klass

def say_foo(self):
    print('bar')

Foo = factory2(say_foo)
foo = Foo()
foo.say_foo()