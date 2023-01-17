

class Node:
    def __init__(self):
        self.left_pointer = None
        self.right_pointer = None
        self.value = None


root = Node()


tree = []

for i in range(10):
    tree.append(Node())








root_pointer = None
next_pointer = 0




def insert(value):
    global tree
    global root_pointer
    global next_pointer

    if root_pointer is None:
        root_pointer = 0
        tree[next_pointer].value = value
        next_pointer += 1
    else:
        tree[next_pointer].value = value
        placed = False
        current_pointer = root_pointer

        while not placed:
            if value > tree[current_pointer].value:
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

print_tree()
insert(10)
insert(11)
insert(9)
insert(8)
insert(7)
insert(0)
print_tree()

