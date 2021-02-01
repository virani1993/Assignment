lines = []
while True:
    snt = input("Enter your line here: ")
    if snt:
        lines.append(snt.upper())
    else:
        break

for snt in lines:
    print(snt)
