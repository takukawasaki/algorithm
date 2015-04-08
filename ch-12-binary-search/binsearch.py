#!ipython3

class Node:
    def __init__(self, x):
        self.data  = x
        self.left  = None
        self.right = None


def search(node, x):
    while node:
        if node.data == x:
            return True
        if x < node.data:
            node = node.left
        else:
            node = node.right
    return False

def insert(node, x):
    if node == None:
        return Node(x)
    elif x == node.data: return node
    elif x < node.data:
        node.left = insert(node.left, x)
    else:
        node.right = insert(node.right, x)
    return node


def search_min(node):
    if node.left == None:
        return node.data
    return search_min(node.left)

# 最小値を削除する
def delete_min(node):
    if node.left == None:
        return node.right
    node.left = delete_min(node.left)
    return node


def delete(node, x):
    if node:
        if x == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.data = search_min(node.right)
                node.right = delete_min(node.right)
        elif x < node.data:
                node.left = delete(node.left, x)
        else:
            node.right = delete(node.right, x)
    return node

def traverse_h(func, node):
    if node:
        traverse_h(func, node.left)
        func(node.data)
        traverse_h(func, node.right)

def print_data(x): print (x)

def loop_insert(node,L):
    for i in L:
        insert(node,i)
    return node


def traverse(node):
    if node:
        for x in traverse(node.left):
            yield x
        yield node.data
        for x in traverse(node.right):
            yield x
                
