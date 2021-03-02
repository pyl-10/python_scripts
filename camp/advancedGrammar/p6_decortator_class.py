# class myClass(object):
#     def __init__(self, number):
#         self.number = number

#     def display(self):
#         print('number is ', self.number)


# six = myClass(6)
# for i in range(1, 5):
    # six.display()

# 装饰类
def decorator(aClass):
    class newClass(object):
        def __init__(self, args):
            self.times = 0
            self.wrapped = aClass(args)

        def display(self):
            # 将 runtimes() 替换为 display()
            self.times += 1
            print('run times', self.times)
            self.wrapped.display()
    return newClass

@decorator
class myClass(object):
    def __init__(self, number):
        self.number = number
    # 重写 display
    def display(self):
        print('number is', self.number)

six = myClass(6)
for i in range(5):
    six.display()