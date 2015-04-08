#!ipython3

def bubblesort (L):
    size = len (L)
    for i in range (size):
        for j in range (size-1,i-1,-1):
            if L [j] < L [j-1]:
                temp = L [j]
                L [j] = L [j-1]
                L [j-1] = temp
                
    return L 
           
