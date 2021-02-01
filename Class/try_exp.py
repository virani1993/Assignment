try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    def fun(a,b):
        c = a/b
        print(c)

    fun()

except:
    print("You can not divide number with 0.")