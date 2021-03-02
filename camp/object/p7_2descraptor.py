class Human(object):
    def __init__(self) -> None:
        self._gender = None

    # 将方法封装成属性
    @property
    def gender2(self):
        print(self._gender)

    # 支持修改
    @gender2.setter
    def gender2(self, value):
        self._gender = value

    # 支持删除
    @gender2.deleter
    def gender2(self):
        del self._gender

h = Human()
h.gender = 'F'
h.gender
del h.gender

# 另一种 property 的写法
# gender = property(get_, set_, del_, 'other property')

# 用装饰函数 建议使用相同的gender2
# 使用 setter 并不能真正意义上实现无法写入，gender 被改名为  _Article__gender

# property 本质并不是函数，而是特殊类（实现了数据描述符的类）
# 如果一个对象同时定义了 __get__() 和 __set__() 方法，则称为数据描述符
# 如果仅定义了 __get__() 方法， 则称为非数据描述符

# property 的优点：
# 1 代码更简洁，可读性，可维护性更强
# 2 更好管理属性的访问
# 3 控制属性的访问权限，提高数据安全性