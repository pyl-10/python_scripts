# 官方文档中装饰器的其他用途案例
# 向一个函数添加属性
def attrs(**kwds):
    def decorate(f):
        for k in kwds:
            setattr(f, k, kwds[k])
        return f
    return decorate

@attrs(versionadded='2.2', author='van ross')
def myMethod(f):
    pass

myMethod(12)

class MyClassOld:
    def __init__(self, var_a, var_b) -> None:
        self.var_a = var_a
        self.var_b = var_b

from dataclasses import dataclass
@dataclass
class MyClass:
    var_a: str
    var_b: str

var_1 = MyClassOld('x', 12)
var_2 = MyClass('x', 12)
print(var_1 == var_2)
print(var_2.var_a)
print(var_2.var_b)