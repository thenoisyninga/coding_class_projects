myList = [12, 11, 13, 5, 6]


def insertion_sort():
    for i in range(1, len(myList)):
        key = myList[i]
        j = i - 1

        while j >= 0 and key > myList[j]:
            myList[j + 1] = myList[j]
            j -= 1
        myList[j + 1] = key


print(myList)
insertion_sort()
print(myList)
