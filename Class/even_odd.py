def showNumbers(limit):
    for i in range(limit+1):
        if i%2==0:
            print(i,"EVEN")

        else:
            print(i,"ODD")
limit = int(input("Enter your Limit: "))

print(showNumbers(limit))

    