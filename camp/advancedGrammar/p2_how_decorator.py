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

print(content())