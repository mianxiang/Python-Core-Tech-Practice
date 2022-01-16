def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(message):
    print(message)

@my_decorator
def byebye(name, message):
    print('{} {}'.format(name, message))

@my_decorator
def great():
    print('today is a great day')

greet('hello world')
byebye('zhzhe', 'see you later')
great()