from  functools import reduce

a =reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7,], 0)

print(a)