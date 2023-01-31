
arrayData = [
    10,
    5,
    6,
    7,
    1,
    12,
    13,
    15,
    21,
    8,
]


def linearSearch(searchValue):
    found = False
    index = 0
    while not found or index > 9:
        if arrayData[index] == searchValue:
            found = True
        index += 1

    return found


# num1 = int(input("Enter a number to search in list: "))
#
# found = linearSearch(num1)
#
# if found:
#     print("The value was found.")
# else:
#     print("Value wa not found.")


def bubbleSort():
    global arrayData

    for x in range(10):
        for y in range(9):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp


print(arrayData)
bubbleSort()
print(arrayData)