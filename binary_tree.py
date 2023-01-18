class Node:
    def __init__(self):
        self.left_pointer = None
        self.right_pointer = None
        self.value = None

tree = []

for i in range(10):
    tree.append(Node())

root_pointer = None
next_pointer = 0


def insert(insert_value):
    global tree
    global root_pointer
    global next_pointer

    if root_pointer is None:
        root_pointer = 0
        tree[next_pointer].value = insert_value
        next_pointer += 1
    else:
        tree[next_pointer].value = insert_value
        placed = False
        current_pointer = root_pointer

        while not placed:
            if insert_value > tree[current_pointer].value:
                if tree[current_pointer].right_pointer is not None:
                    current_pointer = tree[current_pointer].right_pointer
                else:
                    tree[current_pointer].right_pointer = next_pointer
                    placed = True
                    next_pointer += 1
            else:
                if tree[current_pointer].left_pointer is not None:
                    current_pointer = tree[current_pointer].left_pointer
                else:
                    tree[current_pointer].left_pointer = next_pointer
                    placed = True
                    next_pointer += 1

def print_tree():
    global tree
    for node in tree:
        print(f"{node.left_pointer} {node.value} {node.right_pointer}")
    print("")

def search(search_value):
    global tree
    global root_pointer

    current_pointer = root_pointer
    found = False

    while not found:
        if current_pointer is None:
            break
        else:
            if search_value == tree[current_pointer].value:
                found = True
            elif search_value > tree[current_pointer].value:
                current_pointer = tree[current_pointer].right_pointer
            else:
                current_pointer = tree[current_pointer].left_pointer

    return found


insert(10)
insert(12)
insert(11)
insert(4)
insert(1)
insert(6)
insert(78)
print_tree()

print(search(0))