from functools import wraps


# class MyClass(object):
#     def __init__(self, var='init_var', *args, **kwargs) -> None:
#         self._v = var
#         super(MyClass, self).__init__(*args, **kwargs)

#     def __call__(self, func):
#         # 类的函数装饰器
#         @wraps(func)
#         def wrapped_function(*args, **kwargs):
#             func_name = func.__name__ + ' was called'
#             print(func_name)
#             return func(*args, **kwargs)
#         return wrapped_function


# # @MyClass(100)
# def myFunc():
#     pass

# MyClass(100)(myFunc)()

# 另一个示例
class Count(object):
    def __init__(self, func):
        self._func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'num of call is {self.num_calls}')
        return self._func(*args, **kwargs)

@Count
def example():
    print('hello')

example()