a={1:10,2:20} 

b={3:30,4:40}
def Conc(a,b):
    return (a.update(b))

result = Conc(a,b)
print (a)
