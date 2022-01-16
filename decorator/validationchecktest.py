import functools

def validation_check(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args != None and "" != args[0]:
            print(args[0])
            func(*args, **kwargs)
        else:
            raise Exception('input is None or empty, please check them.')
    return wrapper

@validation_check
def neural_network_training(params):
    print('Start to neural network training')


neural_network_training('hello')