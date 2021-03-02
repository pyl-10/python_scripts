class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f'hello, {self.first_name} {self.last_name}'

    def __repr__(self) -> str:
        return f'hello, {self.first_name} {self.last_name}'

me = Person('yin', 'willson')
print(f'{me}')