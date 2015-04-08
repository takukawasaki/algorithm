x#!ipython3
import sys

def oddp (i):
    if i % 2 == 1:
        return True 
    else:
        return False

def parent (i):
    return int ((i-1)/2)


def left (i):
    return 2*i + 1

def right (i):
    return (2*i) + 2

def max_heapfy (L,size,i):
    l = left (i)
    r = right (i)
    temp = L [i]
    if l < size and L [l] > L [i]:
        largest = l
    else:
        largest = i

    if r < size and L [r] > L [largest]:
        largest = r
    if largest != i:
        
        L [i] = L [largest]
        L [largest] = temp
        max_heapfy (L,size,largest)
    return L
    

def min_heapfy (L,size,i):
    
    l = left (i)
    r = right (i)
    temp = L [i]
    if l < size and L [l] < L [i]:
        minimum = l
    else:
        minimum = i

    if r < size and L [r] < L [minimum]:
        minimum = r
    if minimum != i:
        
        L [i] = L [minimum]
        L [minimum] = temp
        min_heapfy (L,size,minimum)
    
    return L

def build_max_heap (L):
    size = len (L)
    for i in range (int (size/2) ,-1,-1):
        max_heapfy (L,size,i)
    return L

def build_min_heap (L):
    size = len (L)
    for i in range (int (size/2) ,-1,-1):
        min_heapfy (L,size,i)
    return L


def heapsort (L):
    size = len (L)
    build_max_heap (L)
    for i in range (len (L)-1,0,-1):
       temp = L [0]
       L [0] = L [i]
       L [i] = temp
       size -= 1
       max_heapfy (L,size,0)
    return L
        
        
#max優先度付きキュー
def heap_maximum(L):
    return L[0]

def heap_extract_max(L,size):
   
    if size < 1:
        print("error: heap-underflow")
                
    max_val = L[0]
    L[0] = L[size-1]
    size -= 1
    max_heapfy(L,size,0)
    return max_val


def heap_increase_key(L,i,key):
    if key < L[i]:
        print("error: new key is smaller than now key")
        sys.exit()
    L[i] = key
    while i > 0 and L[parent(i)] < L[i]:
        temp = L[i]
        L[i] = L[parent(i)]
        L[parent(i)] = temp
        i = parent(i)

    return L


def max_heap_insert(L,key,size):
    size += 1
    L.append( - float("inf"))
    heap_increase_key(L,size-1,key)
    return L
    
def build_max_heap_new(L):
    size = 1
    for i in range(1,len(L)):
        max_heap_insert(L,L[i],size)
    return L
