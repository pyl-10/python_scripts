class Human2(object):
    def __init__(self) -> None:
        self.age = 18

    # 不会处理已存在的属性
    def __getattr__(self, item):
        print('Human2:__getattr__')
        return 'Err 404, 你请求的参数不存在'

    # 会处理已存在的属性（性能损耗）
    def __getattribute__(self, item):
        print('Human2:__getattribute__')
        return super().__getattribute__(item)

h1 = Human2()
# 如果同时存在，执行顺序为 __getattribute__ > __getattr__ > __dict__
print(h1.age)
print(h1.noattr)
