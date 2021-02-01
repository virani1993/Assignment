a = input("Enter your 1st string: ")
b = input("Enter your 2nd string: ")

def count(x):
    for i in range(len(x)):
        i += 1
    return i

a_count = count(a)
b_count = count(b)
print(a_count)
print(b_count)

if a_count>b_count:
    print("1st String is bigger with ",a_count)
    print(a)

elif a_count<b_count:
    print("2nd String is bigger with ",b_count)
    print(b)

elif a_count==b_count:
    print("both has same length")

else:
    pass