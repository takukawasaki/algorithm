#!ipython3

def binarysearch (v,L):
    mid = int (len (L)/2)
    if v == L [mid]:
        return mid
    elif v < L [mid]:
        return binarysearch (v,L [0:mid])
    else:
        return binarysearch (v,L [mid:])

