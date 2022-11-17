myList = [10, 1, 11, 4, 2, 100, 56]
n = len(myList)

for i in range(n):
    for j in range(n-1):
        if myList[j] > myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]

print(myList)
