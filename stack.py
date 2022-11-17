myStack = []

topOfStack = -1

lengthOfStack = int(input("Enter the size of the stack you need: "))

for i in range(lengthOfStack):
    myStack.append(-1)
print(myStack)


def push(itemToPush):
    global topOfStack
    if topOfStack == len(myStack) - 1:
        print("Stack is full")
    else:
        topOfStack += 1
        myStack[topOfStack] = itemToPush
        print(f"Item {itemToPush} has been inserted successfully")


def pop():
    global topOfStack
    if topOfStack < 0:
        print("Stack is empty")
    else:
        myStack[topOfStack] = -1
        topOfStack -= 1
        print("item removed")


while True:
    print("Here are your options:")
    print("1:Push")
    print("2:Pop")
    print("99:Quit Program")
    choice = int(input("Your choice is 1 or 2 or 99: "))
    if choice == 1:
        pushItem = int(input("What do you want to push? "))
        push(pushItem)
    elif choice == 2:
        pop()
    elif choice == 99:
        print("Quitting Program.....")
        break
    else:
        print("Invalid choice")

    print(myStack)
