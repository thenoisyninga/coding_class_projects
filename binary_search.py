MyList = [2, 4, 6, 8, 10]

top = 0
bottom = len(MyList) - 1
Mid = 0
searchItem = int(input("What do you want to search?"))
found = False

while top <= bottom and not found:
    Mid = int((top + bottom)/2)
    if searchItem == MyList[Mid]:
        found = True
    elif searchItem < MyList[Mid]:
        bottom = Mid - 1
    else:
        top = Mid + 1

if found:
    print(f"The value is found at index {Mid}")
else:
    print("Your value was not found")

