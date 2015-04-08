#!ipython3

def merge (L,R):
    new_L = []
    while L  != [] and R != []:
        if L [0] < R [0]:
            new_L.append (L.pop (0))
        else:
            new_L.append (R.pop (0))

    new_L.extend (L)
    new_L.extend (R)

    return new_L


def merge_sort (L):
    size  = len (L)
    if size  == 1:
        return L
    L1  = merge_sort (L [0:int (size/2)])
    L2  = merge_sort (L [int (size/2):size])
    return merge (L1,L2)

 

    
            
