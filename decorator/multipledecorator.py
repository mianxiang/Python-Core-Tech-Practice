import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)
    return wrapper

def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorate2')
        func(*args, **kwargs)
    return wrapper

@my_decorator1
@my_decorator2
def greet(message):
    print(message)

greet('hello world')
