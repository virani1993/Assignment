a = int(input("Enter number of elements in List"))
List = []
for i in range(a):
    print("Enter yout ", i, "element")
    a = input("")
    List.append(a)
print(List)
def unique(List):
    Set = set(List)
    List = list(Set)
    return List
print(unique(List))
