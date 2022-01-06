import timeit
timeit.timeit('a=list()', number=10000)
timeit.timeit('a=[]', number=10000)  
timeit.timeit('a=()', number=10000)