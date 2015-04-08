#!ipython3

from numpy.random import randint
L = [randint(20) for _ in range(20)] 

def bucketsort(L):
    count = [0 for i in range(max(L) + 1)]
    for value in L:
        count[value] += 1
    L =[]
    for nr, amount in enumerate(count):
        L.extend([nr] * amount)
    return L

def bsort(A):
    """Returns A sorted. with A = {x : x such that 0 <= x < 1}."""
    size = 10
    buckets = [[] for x in range(10)]
    for i, x in enumerate(A):
        buckets[int(x/size)].append(x)
    out = []
    for buck in buckets:
        out += isort(buck)
    
    return out

#リスト内包連結
#out =[i for buck in buckets for i in isort(buck)]

def isort(L):
    size = len(L)
    for i in range(1,size):
        minval = L[i]
        j = i - 1
        while j >= 0 and L[j] > minval:
            temp = L[j]
            L[j] = minval
            L[j + 1] = temp
            j -= 1

    return L




