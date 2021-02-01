
List= [4,66,23,54,7,122,55,66,22,678,1,16,26]
L=S=0
for i in List:
    if i>L :
        L = i
print ("Largest number is ",L)

def Sml(My_List):
    S = List[0]
    for i in My_List:
        if i<S:
            S=i
    print ("Smallest value is ",S)
Sml(List)