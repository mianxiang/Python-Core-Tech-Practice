import time

start_using_plus = time.perf_counter()
s = ''
for n in range(0, 1000000):
    s += str(n)
end_using_plus = time.perf_counter()
print('time elapsed {} using string plus'.format(end_using_plus-start_using_plus))

start_using_join = time.perf_counter()
l = []
for n in range(0, 1000000):
    l.append(str(n))
l = "".join(l)
end_using_join = time.perf_counter()
print('time elapsed {} using string join'.format(end_using_join-start_using_join))
