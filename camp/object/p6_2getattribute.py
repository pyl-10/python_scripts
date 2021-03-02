class Human2(object):
    """
    拦截已存在的属性
    """
    def __init__(self) -> None:
        self.age = 18
    def __getattribute__(self, item):
        print(f'__getattribute__ called item:{item}')
        return super().__getattribute__(item)

h1 = Human2()

print(h1.age)
# 存在的属性返回取值
print(h1.noattr)
# 不存在的属性返回 AttributeError

# 为什么用 super 不用 self ？