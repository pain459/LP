class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    node.height = max(get_height(node.left), get_height(node.right)) + 1

def right_rotate(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def left_rotate(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def balance(node, key):
    balance_factor = get_height(node.left) - get_height(node.right)

    if balance_factor > 1 and key < node.left.key:
        return right_rotate(node)
    if balance_factor < -1 and key > node.right.key:
        return left_rotate(node)
    if balance_factor > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance_factor < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)
    
    return node

def insert(node, key):
    if not node:
        return AVLNode(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    update_height(node)
    return balance(node, key)

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete(node, key):
    if not node:
        return node

    if key < node.key:
        node.left = delete(node.left, key)
    elif key > node.key:
        node.right = delete(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        temp_val = min_value_node(node.right)
        node.key = temp_val.key
        node.right = delete(node.right, temp_val.key)

    update_height(node)
    return balance(node, key)

def search(node, key):
    if not node or node.key == key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)

# Example usage
root = None
keys = [15, 10, 20, 8, 12, 16, 25]

for key in keys:
    root = insert(root, key)

# Perform search
found_node = search(root, 10)
print("Found:", found_node.key if found_node else "Not found")

# Perform deletion
root = delete(root, 10)
found_node = search(root, 10)
print("After deletion, found:", found_node.key if found_node else "Not found")
