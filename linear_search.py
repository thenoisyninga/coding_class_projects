print("=====================================================")
print("===============SEARCHING ALGORITHM===================")
print("=====================================================\n\n")


numList = [2, 4, 9, 10, 2]
searchItem = int(input("What do you want to find? "))

print("\nWhat search option do you want to go for?")
print("[1] Frequency of occurrence of the searchItem in the list")
print("[2] If the value exists and gives the index of the first occurrence")
print("[3] States all the indexes where the search value occurs")
option = int(input("\nWhat do you chosse (1, 2 or 3)? "))
print("")

if option == 1:
    #Gives the frequency of occurrence of the searchItem in the list/
    counter = 0

    for num in numList:
        if num == searchItem:
            counter = counter + 1


    print(f"The number {searchItem} appears {counter} times.")


if option == 2:
    # Checks if the value exists and gives the index of the first occurrence.
    found = False
    lengthOfList = len(numList)
    index = 0

    while not found and index < lengthOfList:
        if numList[index] == searchItem:
            found = True
            print(f"{searchItem} was found on index {index}.")
        index = index + 1
    if found == False:
        print(f"{searchItem} was not found.")


if option == 3:
    # States all the indexes where the search value occurs.
    for i in range(len(numList)):
        if numList[i] == searchItem:
            print(f"{searchItem}  was found at index {i}.")

