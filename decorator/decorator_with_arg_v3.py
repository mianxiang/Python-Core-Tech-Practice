import functools

def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(3)
def greet(message):
    print(message)

greet('hello hangzhou')
print(greet.__name__)
print(help(greet))