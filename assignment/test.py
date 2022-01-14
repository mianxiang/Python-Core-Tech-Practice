l1 = [1, 2, 3]
l2 = [1, 2, 3]
l3 = l2

if l3 is l2:
    print('Both of {} and {} are the same object:{}-{}'.format(l2, l3, id(l2), id(l3)))
else:
    print('{} and {} are different object:{}-{}'.format(l2, l3, id(l2), id(l3)))


if l1 is l2:
    print('Both of {} and {} are the same object:{}-{}'.format(l2, l1, id(l2), id(l1)))
else:
    print('{} and {} are different object:{}-{}'.format(l2, l1, id(l2), id(l1)))

    
