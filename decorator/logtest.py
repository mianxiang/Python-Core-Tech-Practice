import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper

@log_execution_time
def calculate_result(count):
    sum = 0
    for i in range(count):
        sum += i
    return sum


calculate_result(1000)
calculate_result(1000000)
calculate_result(10000000)