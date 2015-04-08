#!ipython3




def stack_empty(L):
    size = len (L)
    if size  == 0:
        return True
    else :
        return False

def push(L,x):
    L.append(x)

def poppy(L):
    top = len(L) - 1
            
    if stack_empty(L):
        raise ValueError('no values in L')
    else:
        del L[-1]


class stack:
    def __init__(self,data=[]):
        self.data=data

    def stack_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False

    def push(self,x):
        self.data.append(x)

    def pop(self):
        if self.stack_empty():
            print( 'stack is empty')
        else:
            num=len(self.data)-1
            result=self.data[num]
            self.data=self.data[0:num]
            return result



def que(L,x):
    L.append(x)
    del L[0]
    return L    

def dque(L):
    del L[0]
    return L

            
#連結リストの制作
#高階関数として表現している

    
def cons(a,b):
    def dispatch(m):
        if m == 0: return a
        elif m == 1: return b
        else: raise ValueError('oops')
    return dispatch

def car (z):
    return z(0)

def cdr(z):
    return z(1)


def nthcdr (index,L):
    if index == 0:
        return L
    else:
        return nthcdr (index - 1, cdr(L))    

def get_val(index,L):
    try:
        return car(nthcdr(index,L))
    except TypeError:
        print(None)

#リストを作りmake_consの引数にする
def make_cons(L):
    if len(L) == 1:
        return cons(L[0],None)
    else:
        return cons(L[0],make_cons(L[1:]))


import copy
import numpy as np



def insert_cons(L,val,index):
    R = cons(val,nthcdr(index,L))
    return R

#多重配列表現
def make_list(L):
    size = len(L)
    cl = []
    for i in range(size):
        cl.append([i-1,L[i],i+1])
    cl[0][0] = None
    cl[-1][2] = None
    return cl

L = make_list([1,2,3,4])

def list_search(L,k):
    size = len(L)
    for i in range(size):
        if L[i][1] == k:
            return L[i-1][2],L[i+1][0]
        else:
            raise ValueError("not in it")

def list_insert(L,x):
    L.insert(0,[None,x,1])
    for i in range(len(L[1:])):
        if L[i+1][0] == None:
            L[i+1][0] = 0
        else:
            L[i+1][0] += 1
        if L[i+1][2] == None:
            L[i+1][2] = None
        else:
            L[i+1][2] += 1

    return L        


#Deque とは、スタックとキューを一般化したもの
#indexing OK

from collections import deque
d = deque('ghi')
d.append('j')
d.appendleft('f')
d.popleft()
d.pop()


def deq_insert(L,idex,v):
    L.insert(idex,v)
    return L
