class Node:
    def __init__(self, data, pointer):
        self.data = data
        self.pointer = pointer


linked_list = []

linked_list.append(Node(20, 4))
linked_list.append(Node(5, 3))
linked_list.append(Node(0, 1))
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


def print_data():

    current_pointer = head

    while current_pointer is not None:
        print(linked_list[current_pointer].data)
        current_pointer = linked_list[current_pointer].pointer


def search(search_value):

    current_pointer = head
    found = False

    while current_pointer is not None and not found:
        if search_value == linked_list[current_pointer].data:
            found = True
        current_pointer = linked_list[current_pointer].pointer

    return found


def delete(delete_value):
    global head
    global linked_list

    if linked_list[head].data == delete_value:
        head = linked_list[head].pointer
    else:
        previous_pointer = head
        current_pointer = linked_list[head].pointer
        deleted = False
        while current_pointer is not None and not deleted:
            if delete_value == linked_list[current_pointer].data:
                linked_list[previous_pointer].pointer = linked_list[current_pointer].pointer
                deleted = True
            previous_pointer = current_pointer
            current_pointer = linked_list[current_pointer].pointer


def insert(insert_value):
    global linked_list
    global head
    global next_pointer

    linked_list.append(Node(insert_value, None))

    if insert_value < linked_list[head].data:
        linked_list[next_pointer].pointer = head
        head = next_pointer
        next_pointer += 1
    else:
        previous_pointer = head
        current_pointer = linked_list[head].pointer
        placed = False

        while not placed:
            if current_pointer is None:
                linked_list[previous_pointer].pointer = next_pointer
                placed = True
                next_pointer += 1
            else:
                if insert_value < linked_list[current_pointer].data:
                    linked_list[previous_pointer].pointer = next_pointer
                    linked_list[next_pointer].pointer = current_pointer
                    placed = True
                    next_pointer += 1

                previous_pointer = current_pointer
                current_pointer = linked_list[current_pointer].pointer
