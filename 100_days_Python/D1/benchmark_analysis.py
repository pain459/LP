import random
import time

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
    if not node:
        return node
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

def search(node, key):
    if not node or node.key == key:
        return node
    elif key < node.key:
        return search(node.left, key)
    else:
        return search(node.right, key)

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

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bst_insert(node, key):
    if not node:
        return BSTNode(key)
    elif key < node.key:
        node.left = bst_insert(node.left, key)
    else:
        node.right = bst_insert(node.right, key)
    return node

def bst_search(node, key):
    if not node or node.key == key:
        return node
    elif key < node.key:
        return bst_search(node.left, key)
    else:
        return bst_search(node.right, key)

def bst_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def bst_delete(node, key):
    if not node:
        return node
    if key < node.key:
        node.left = bst_delete(node.left, key)
    elif key > node.key:
        node.right = bst_delete(node.right, key)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        temp_val = bst_min_value_node(node.right)
        node.key = temp_val.key
        node.right = bst_delete(node.right, temp_val.key)
    return node

def generate_test_data(n):
    return [random.randint(1, 10000) for _ in range(n)]

def benchmark(tree_type, operations, data):
    start_time = time.time()
    root = None
    for op, key in zip(operations, data):
        if op == 'insert':
            if tree_type == 'bst':
                root = bst_insert(root, key)
            elif tree_type == 'avl':
                root = insert(root, key)
        elif op == 'search':
            if tree_type == 'bst':
                bst_search(root, key)
            elif tree_type == 'avl':
                search(root, key)
        elif op == 'delete':
            if tree_type == 'bst':
                root = bst_delete(root, key)
            elif tree_type == 'avl':
                root = delete(root, key)
    end_time = time.time()
    return end_time - start_time

# Example of running the benchmark
n = 1000  # Number of operations
data = generate_test_data(n)
operations = ['insert'] * (n//2) + ['search'] * (n//4) + ['delete'] * (n//4)
random.shuffle(operations)

bst_time = benchmark('bst', operations, data)
avl_time = benchmark('avl', operations, data)

print(f"BST Time: {bst_time:.4f} seconds")
print(f"AVL Time: {avl_time:.4f} seconds")
