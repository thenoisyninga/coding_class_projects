myList = []

# Data Assembly

for item in range(10):
    validitem = False
    while not validitem:
        x = float(input("Enter item:"))
        if x >10 or x <= 0:
            print("invalid input,input again")
        else:
            validitem = True
            myList.append(x)
    print(myList)

# Processing Data

total = 0
for item in myList:
    total += item

average = total/10
print(f"The average is: {average}")

if average < 5:
    print("The values are lower")
elif average > 5:
    print("the values are higher")
else:
    print("the values are moderate")
