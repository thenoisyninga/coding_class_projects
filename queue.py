
top = -1
bottom = -1

myQueue = []

topOfQueue = -1

lengthOfQueue = int(input("Enter the size of the queue you need: "))

for i in range(lengthOfQueue):
    myQueue.append(None)
print(myQueue)


def insert(itemToInsert):
    global top
    global bottom
    if (bottom == top + 1) or ((top == lengthOfQueue - 1) and (bottom == 0)):
        print("The Queue is full.")
    else:
        if top == -1:
            bottom = 0
        if top == lengthOfQueue -1:
            top = 0
        else:
            top = top + 1
        myQueue[top] = itemToInsert


def delete():
    global bottom
    global  top
    willBeEmpty = (bottom == top)
    if top == -1:
        print("Queue is empty.")
    else:
        myQueue[bottom] = None
        if bottom == lengthOfQueue -1:
            bottom = 0
        else:
            bottom = bottom + 1
    if willBeEmpty:
        top = -1
        bottom = -1

while True:
    print("Here are your options:")
    print("1:Insert")
    print("2:Delete")
    print("99:Quit Program")
    choice = int(input("Your choice is 1 or 2 or 99: "))
    if choice == 1:
        insertItem = int(input("What do you want to insert? "))
        insert(insertItem)
    elif choice == 2:
        delete()
    elif choice == 99:
        print("Quitting Program.....")
        break
    else:
        print("Invalid choice")

    print(myQueue)
