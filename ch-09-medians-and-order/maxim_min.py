#!ipython3
from quicksort import partition
from quicksort import randomized_partition
import quicksort
import random

def minimum(L):
    min_val = L[0]
    for i in range(1,len(L)):
        if min_val > L[i]:
            min_val = L[i]

    return min_val

def randomized_select(L,p,r,i):
    if p == r:
        return L[p]
    q = randomized_partition(L,p,r)
    k = q - p + 1
    if i == k:
        return L[q]
    elif i < k:
        return randomized_select(L,p,q-1,i)
    else:
        return randomized_select(L,q+1, r, i-k )

def selection(L,p,r,i):
    if p == r:
        return L[p]
    q= partition(L,p,r)
    k = q - p + 1
    if i == k:
        return L[q]
    elif i < k:
        return selection(L,p,q-1,i)
    else:
        return selection(L,q+1, r, i-k )
        
