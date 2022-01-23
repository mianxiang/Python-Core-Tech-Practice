import time
import threading
import concurrent.futures

def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def calculate_sums(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(cpu_bound, numbers)

def main():
    start_time = time.perf_counter()
    nums = [10000000 + x for x in range(20)]
    calculate_sums(nums)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))

if __name__ == '__main__':
    main()