MyList = [2, 4, 6, 8, 10]

top = 0
bottom = len(MyList) - 1


searchItem = int(input("What do you want to search?"))
found = False

while top <= bottom and not found:
    
    mid = int((top + bottom)/2)
    
    if searchItem > MyList[mid]:
        top = mid + 1
    elif searchItem < MyList[mid]:
        bottom = mid - 1
    else:
        found = True

if found:
    print(f"The value is found at index {mid}")
else:
    print("Your value was not found")

