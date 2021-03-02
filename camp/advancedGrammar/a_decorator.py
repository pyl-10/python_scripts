
from flask import Flask

# 装饰器， @ 语法糖


@decorate
def fun2():
    print('do sth')

# 等效于下面


def fun2():
    print('do sth')


fun3 = decorate(fun2)

# 装饰器在模块导入的时候自动运行
# testmodule.py


def decorate(func):
    print('running in modlue')

    def inner():
        return func()
    return inner


@decorate
def func2():
    pass


# 用在哪里
# Flask 的装饰器是怎么用的？
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>hello world </h1>'

# app.add_url_rule('/', 'index')


if __name__ == '__main__':
    app.run(debug=True)

# 注册


@route('index', methods=['GET', 'POST'])
def static_html():
    return render_template('index.html')


# 等效于
static_html = route('index', methods=['GET', 'POST'])(static_html)()

# 包装


def html(func):
    def decorator():
        return f'<html>{func()}</html>'
    return decorator


def body(func):
    def decorator():
        return f'<body>{func()}</body>'
    return decorator


@html
@body
def content():
    return 'hello world'
