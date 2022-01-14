def func(d):
    d['a'] = 10
    d['b'] = 20

def func2(d):
    d = {'c':100}

def func3(d):
    d = {'d':1000}
    return d

d = {'a':1, 'b':2}
func(d)
print(d)

d = {'a':1, 'b':2}
func2(d)
print(d)

d = {'a':1, 'b':2}
d = func3(d)
print(d)