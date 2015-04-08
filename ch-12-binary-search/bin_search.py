#!ipython3


class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.p = None

        
def inorder_tree_walk(func,node):
    if node:
        inorder_tree_walk(func,node.left)
        func(node.data)
        inorder_tree_walk(func,node.right)

def print_data(x):
    print(x)
        
   


        
def tree_search(node,x):
    if node == None or x == node.data:
        return x
    if x < node.data:
        return tree_search(node.left,x)
    else:
        return tree_search(node.right,x)

        

def loop_insert(node,L):
    for i in L:
        tree_insert(node,Node(i))
    return node



def tree_min(node):
    if node.left == None:
        return node.data
    else:    
        return tree_min(node.left)


def tree_max(node):
    if node.right == None:
        return node.data
    else:
        return tree_max(node.right)


def tree_succesor(x):
    if x.right != None:
        return tree_min(x.right)

    y = x.p

    while y != None and x == y.right:
        x = y
        y = y.p
        return y

        
def tree_insert(T,z):
    y = None
    x = T
    while x != None:
        y = x
        if x.data < x.data:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == None:
        T = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z

        
def transplant(T,u,v):
    if u.p == None:
        T = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p


        
def tree_delete(T,z):
    if z.left == None:
        transplant(T,z,z.right)
    elif z.right == None:
        transplant(T,z,z.left)
    else:
        y = tree_min(z.right)
        if y.p != z:
            transplant(T,y,y.right)
            y.right = z.right
            y.right.p = y
        transplant(T,z,y)
        y.left = z.left
        y.left.p = y
