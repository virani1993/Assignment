List = []
temp = int(input("how many values you want to add :"))

for i in range(0,temp):
     x = int(input("Enter your value: "))
     List.append(x)
print(List)

def no_even(L_list):
    for i in L_list:
        if i%2==0:
            List.remove(i)
        
no_even(List)
print("New Non_Even_List :",List)
