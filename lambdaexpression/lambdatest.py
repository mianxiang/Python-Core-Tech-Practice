from functools import reduce

squared = map(lambda x: x**2, [1, 2, 3, 4, 5])
for eachItem in squared:
    print(eachItem)


l = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, l)
for x in new_list:
    print(x)

l2 = [1, 2, 3, 4, 5]
newvalue = reduce(lambda x, y: x * y, l2)
print(newvalue)