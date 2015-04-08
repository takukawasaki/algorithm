#!ipython3

#insert sort
def insertion_sort (L):
    size = len (L)
    for i in range (1,size):
        minval = L [i]
        j = i - 1
        while j >=  0 and L [j] > minval:
            L [j + 1] = L [j]
            j -= 1
        L [j + 1] = minval
    return L
            
def linear_search (v,L):
    size = len (L)
    for i in range (size):
        if L [i] == v:
            return L [i],i
        else:
            print ('there is no shit in it')
    


#再帰版挿入ソート
def isort (L):  
    if L == []:
        return L
    else:
        x =L [0]
        y=L [1:]
        return insert (x,isort (y))


def insert (x,y):
    if y == []:
        return  [x]
    
    if x <  y [0]:
        return [x,y [0]] + y [1:]
    else:   
        return [y [0]] + insert (x, y [1:])
    

				
			







