#!ipython3

import binsearch

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self,x):
        return binsearch.search(self.root,x)

    def insert(self,x):
        self.root =  binsearch.insert(self.root,x)

    def delete(self,x):
        self.root =  binsearch.delete(self.root,x)

    def traverse(self):
        for x in binsearch.traverse(self.root):
            yield x
