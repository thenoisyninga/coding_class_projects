

class Node:
    def __init__(self):
        self.Left_pointer = None
        self.right_pointer = None
        self.value = None

tree = []
root_pointer = None

def insert_node(new_value):

    global tree
    global root_pointer

    if root_pointer is None:
        tree.append(new_value)
        root_pointer = 0
    else:
        new_node = Node()
        new_node.value = new_value
        tree.append(new_node)
        new_pointer = tree.index(new_node)
        placed = False
        current_pointer = root_pointer

        while not placed:
            if tree[new_pointer].value > tree[current_pointer].value:
                if tree[current_pointer].right_pointer is None:
                    tree[current_pointer].right_pointer = new_pointer
                    placed = True
                else:
                    current_pointer = tree[current_pointer].right_pointer
            else:
                if tree[current_pointer].left_pointer is None:
                    tree[current_pointer].left_pointer = new_pointer
                    placed = True
                else:
                    current_pointer = tree[current_pointer].left_pointer