class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer

linked_list = []

linked_list.append(Node(20, 4))
linked_list.append(Node(5, 3))
linked_list.append(Node(0, 3))
linked_list.append(Node(9, 6))
linked_list.append(Node(25, 5))
linked_list.append(Node(78, None))
linked_list.append(Node(13, 0))

head = 2
next_pointer = 7
def show_linked_list():
    i = 0
    print(f"head --> {head}")
    print("Index Data  Pointer")
    for node in linked_list:
        print(f"[{i}]   {node.data}" + ("  " if len(str(node.data)) == 1 else " ") + f"-> {node.pointer}")
        i += 1

show_linked_list()


print(search(100))