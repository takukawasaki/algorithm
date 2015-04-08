#!ipython3

class Cons(object):
    
    def cons(self,a,b):
        def dispatch(m):
            if m == 0: return a
            elif m == 1: return b
            else: raise ValueError('oops')
        return dispatch

    def car (self,z):
        return self.z(0)

    def cdr(self,z):
        return self.z(1)


def nthcdr (index,L):
    if index == 0:
        return L
    else:
        return nthcdr (index - 1, Cons.cdr(L))    

def get_val(self,index,L):
    try:
        return car(nthcdr(index,L))
    except TypeError:
        print(None)

    #リストを作りmake_consの引数にする
def make_cons(self,L):
    if len(L) == 1:
        return cons(L[0],None)
    else:
        return cons(L[0],make_cons(L[1:]))


import copy

def push(L,value):
    
    R = cons(value,L)
    R1 = copy.deepcopy(R)
    return R


    
def insert_cons(L,val,index):
    R = cons(val,nthcdr(index,L))
    return R





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
