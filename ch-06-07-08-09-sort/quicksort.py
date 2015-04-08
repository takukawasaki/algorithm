#!ipython3

L = [2, 8, 7, 1, 3, 5, 6, 4]

def quicksort(L):
    size = len(L)
    if size <= 1:
        return L

    pivot = L[0]
    new_L =[]
    new_R = []
    for i in range(1,size):
        if L[i] <= pivot:
            new_L.append(L[i])
        else:
            new_R.append(L[i])
            
    return quicksort(new_L) + [pivot] + quicksort(new_R)

def quicksort2(L):
    size = len(L)
    if size <= 1:
        return L

    pivot = L[0]
    new_L = []
    new_R = []
    for i in range(1,size):
        if L[i] <= pivot:
            new_L.append(L[i])
        else:
            new_R.append(L[i])
            
    return quicksort2(new_L) + [pivot] 



def partition (L,p,r):
    x = L[r]
    i = p -1
    for j in range(r):
        if L[j] <= x:
            i += 1
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

    temp2 = L[i + 1]
    L[i + 1] = L[r]
    L[r] = temp2
    return i + 1
            
    
def qsort(L):
    size = len(L)
    if size <= 1:
        return L

    return qsort([i for i in L[1:] if i < L[0]]) + L[0:1] \
         + qsort([j for j in L[1:] if j >= L[0]])


             
                       
def quicksort_rev(L):
    size = len(L)
    if size <= 1:
        return L

    pivot = L[size-1]
    new_L =[]
    new_R = []
    for i in range(size-2,-1,-1):
        if L[i] >= pivot:
            new_L.append(L[i])
        else:
            new_R.append(L[i])
            
    return quicksort_rev(new_L) + [pivot] + quicksort_rev(new_R)


import numpy as np
from numpy import random

def randomized_partition(L,p,r):
    i = random.randint(p,r+1)
    temp = L[r]
    L[r] = L[i]
    L[i] = temp
    return partition(L,p,r)
    
def hoare_partation(L,p,r):
    x = L[p]
    i = p - 1
    j = r + 1
    
    while True:
        while True:
            j -= 1
            if L[j] <= x:
                break

        while True:
            i += 1
            if L[i] >= x:
                break
        
        if i < j:
            temp = L[i]
            L[i] = L[j]
            L[j] = temp
        else:
            return j

def qsort_slow(myList, start, end):
    if start < end:
        pivot = hoere_partition(myList, start, end)
        qsort_slow(myList, start, pivot-1)
        qsort_slow(myList, pivot+1, end)
    return myList

        

def hoere_partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right
