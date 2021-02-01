'''List = []
for i in range(1,31):
    i = i*i
    List.append(i)
print(List)'''

#a = map(lambda i : i*i, range(1,31))
#print(list(a))


#a = filter(lambda i : i%2==0, range(1,50))
#rint(list(a))

from functools import reduce
a = reduce(lambda i,j : i+j, range(1,50))
print(a)


