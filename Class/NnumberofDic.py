a = int(input("Enter Your n number for dictionary : "))
dic = {}
for i in range(1,a+1):
    items = {i:i*i}
    dic.update(items)
print(dic)
