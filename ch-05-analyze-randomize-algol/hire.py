#!ipython3

import numpy as np
from numpy import random

def hire_assistant (n):
    best = 0
    person = random.rand (n) * 10
    for i in range (n):
        if best < person [i]:
            best = person [i]
    return best ,i

def permute_by_sorting (L):
    size = len (L)
    P=[]
    for i in range (size):
        P.append (random.randint (1,pow (size,3)))
    sort_index = list (np.argsort (P))
    return P,sort_index ,[L [x] for x in sort_index]

def permute_by_sorting2 (L):
    size = len (L)
    P=[]
    for i in range (size):
        P.append (random.randint (1,pow (size,3)))
    index = sorted (range (len (P)), key=lambda k: P[k])
    return P,index,[L [x] for x in index]


def randomize_in_place_old (L):
    size = len (L)
    for i in range (size):
        temp = L [i]
        random_number = random.randint (i,size)
        L [i] = L [random_number]
        L [random_number] =  temp
    return L

def randomize_in_place (L):
    random.shuffle (L)
    return L

def permute_without_identity (L):
    size = len (L)
    for i in range (size):
        L [i] = L [random.randint (1,size)]            
    return L  
        
def permute_by_cyclic (L):
    size = len (L)
    B = []
    offset = random.randint (0,size)
    for i in range (size):
        dest = i + offset
        if dest > size:
            dest -= size
        B.insert (dest,L [i])
    return B



def random_sample (m,n):
    S1 = set (range (m))
    S2 = set (range (n))
    if m == 0:
        return set ()
    else:
        S = random_sample (m-1,n-1)
        i = random.randint (0,n)
        if i in S:
            S = S.union (S2)
        else:
            S = S.union (set (range (i)))
        return S

def score (i):
    score = random.randint (100)
    return score

def on_line_maximum (k,n):
    bestscore = - float ("inf")
    for i in range (k):
        if score (i) > bestscore:
            bestscore = score (i)
    for i in range (k,n):
        if score (i) > bestscore:
            return i
    return n

def fibo (n):
    return fibo_iter (1,0,n)

def fibo_iter (a,b,n):
    if n == 0:
        return b
    else:
        return fibo_iter (a+b ,a,(n-1))
    

def random_search (x,L):
    size = len (L)
    if size != 0:
        index = random.randint (size)
    try:
        if L [index] == x :
            return index,L [index]
        elif L == []:
            return print ("empty")
        else :
            L.pop (index)
            return random_search (x,L)    
    except:
        ValueError (print ("not in it"))


def deterministic_search (x,L,counter = 0):
    size = len (L)
    if L == []:
        print ('not in it')
    elif L [0] == x:
        return counter
    else:
        return deterministic_search (x,L [1:],counter + 1)


