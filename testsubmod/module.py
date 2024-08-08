def hello(name: str):
    print(f'hello, {name}')

class Person:
    def __init__(self, name: str):
        self._name = name
    def greet(self):
        hello(self._name)

if __name__ == '__main__':
    p = Person('dt')
    p.greet()
