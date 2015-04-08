#!ipython3
from numpy.random import randint
import numpy.random as nr
import numpy as np
L = [randint(20) for _ in range(20)]
A = [[5,8,3],
     [3,10,1],
     [2,1,9]] 
N = np.array(A)

def compare_exchange(L,i,j):
    if L[i] < L[j]:
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
    return L

def isort(L):
    size = len(L)
    for j in range(size):
        for i in range(size-1,j,-1):
            compare_exchange(L,i,j)
    return L


def compare_exchange1(L,i,j):
    if L[i][j] < L[j][j]:
        temp = L[i][j]
        L[i][j] = L[j][j]
        L[j][j] = temp
    return L


def isort_col(L):
    L.sort(0)
    L = L.T
    L.sort(0) 
    return L


def ispo(L):
    size = len(L)
    N = [ [] for _ in range(size)]
    for i in range(size):
        for j in range(len(L[0])):
            N[i].append(L[j][i])    
    for i in N:
        isort(i)
       
        
    return N



    
        
        

