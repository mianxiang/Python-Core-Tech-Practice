import os
import psutil

def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def func():
    show_memory_info('initial')
    a = [i for i in range(100000)]
    show_memory_info('after a created')

if __name__ == '__main__':
    func()
    show_memory_info('finished')