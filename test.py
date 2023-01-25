class Node:
    def __init__(self):
        self.left_pointer = None
        self.right_pointer = None
        self.value = None

tree = []

for i in range(10):
    tree.append(Node())

root_pointer = 0
next_pointer = 1

tree[0].value = 100
tree[0].left_pointer = 1
tree[1].value = 12

def print_tree():
    global tree
    print(f"root_pointer --> {root_pointer}")
    print(f"next_pointer --> {next_pointer}")
    print("")
    print("-----------")
    print("    L Val R")
    print("-----------")
    n = 0
    for node in tree:
        print(f"[{n}] {node.left_pointer} {node.value} {node.right_pointer}")
        n += 1
    print("")


def search(search_value):

    global tree
    global current_pointer
    found = False

    while current_pointer is not None and not found:
        if search_value == tree[current_pointer].value:
            found = True
        elif search_value > tree[current_pointer].value:
            current_pointer = tree[current_pointer].right_pointer
        else:
            current_pointer = tree[current_pointer].left_pointer
    return found
print_tree()

print(search(100))



