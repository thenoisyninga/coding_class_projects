class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode


startPointer = 0
emptyList = 5

linkedList = [
    node(1, 1),
    node(5, 4),
    node(6, 7),
    node(7, -1),
    node(2, 2),
    node(0, 6),
    node(0, 8),
    node(56, 3),
    node(0, 9),
    node(0, -1),
]


def outputNodes(theLinkedList, theStartPointer):
    current_pointer = theStartPointer

    while current_pointer != -1:
        print(theLinkedList[current_pointer].data)
        current_pointer = theLinkedList[current_pointer].nextNode


def addNode(linkedList, startPointer, emptyList):
    if emptyList == -1:
        return linkedList, startPointer, emptyList, False
    else:
        insert_value = int(input("Enter the number you want to insert: "))

        linkedList[emptyList].data = insert_value

        current_pointer = startPointer
        placed = False
        while not placed:
            if linkedList[current_pointer].nextNode == -1:
                linkedList[current_pointer].nextNode = emptyList
                new_data_pointer = emptyList
                emptyList = linkedList[new_data_pointer].nextNode
                linkedList[new_data_pointer].nextNode = -1
                placed = True
            current_pointer = linkedList[current_pointer].nextNode

        return linkedList, startPointer, emptyList, True


outputNodes(linkedList, startPointer)

linkedList, startPointer, emptyList, inserted = addNode(linkedList, startPointer, emptyList)
linkedList, startPointer, emptyList, inserted = addNode(linkedList, startPointer, emptyList)

outputNodes(linkedList, startPointer)
