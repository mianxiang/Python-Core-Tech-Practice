def f1():
    print('hello')
    def f2():
        print('world')
    f2()

def factorial(input):
    if not isinstance(input, int):
        raise Exception('input must be an integer')
    if input < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)

print(factorial(5))