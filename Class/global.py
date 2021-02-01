List = [10, 20, 30, 40, 50]
Add = 0
for i in List:
    Add = Add + i
    
print ("Sum of the List = ",Add)

def mul(My_List):
    result = 1
    for i in My_List:
        result = result * i
    return result
Mul = mul(List)
print ("Multiplication is ", Mul)

