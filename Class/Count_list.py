'''a = input("enter your string: ")
List = list(a)
u,l = 0,0
def count_upper_lower():
    u,l = 0,0
    for i in List:
        if i.upper:
            u +=1
        elif i.lower:
            l +=1
        else:
            pass
    print(u)
    print(l)


print(count_upper_lower())'''

word = input("enter your string: ")
lower  = sum(map(str.islower, word))
upper = sum(map(str.isupper, word))
print(lower)
print(upper)
