#!ipython3


def strlist(L):
    a = list(str(L))
    return a



def radixsort00(L):
    size = len(L)
    B = [strlist(L[i]) for i in range(size)]
    C = []
    for i in range(len(B)):
        C.append(B[i][-1])
        return B,C



    
def radixsort( aList ):
    RADIX = 10
    maxlength = False
    tmp , placement = -1, 1
    while not maxlength:
        maxlength = True
            # declare and initialize buckets
        buckets = [list() for _ in range( RADIX )]
            # split aList between lists
        for  i in aList:
            tmp = i / placement
            buckets[int(tmp % RADIX)].append( i )
            if maxlength and tmp > 0 :
                maxlength = False
    
                    # empty lists into aList array
        a = 0
        for b in range( RADIX ):
            buck = buckets[b]
            for i in buck:
                aList[a] = i
                a += 1
                            # move to next digit
        placement *= RADIX
    return aList

# Radix sort for variable length strings
def radixSortString(array):
    maxLen = -1
    for string in array: # Find longest string
        strLen = len(string)
        if strLen > maxLen:
            maxLen = strLen
    oa = ord('a') - 1; # First character code
    oz = ord('z') - 1; # Last character code
    n = oz - oa + 2; # Number of buckets (+empty character)
    buckets = [[] for i in range(0, n)] # The buckets
    for position in reversed(range(0, maxLen)):
        for string in array:
            index = 0 # Assume "empty" character
            if position < len(string): # Might be within length
                index = ord(string[position]) - oa
            buckets[index].append(string) # Add to bucket
        del array[:]
        for bucket in buckets: # Reassemble array in new order
            array.extend(bucket)
            del bucket[:]
    return array
                        
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





if __name__=='__main__':
    try:
        L = [324,546,3124,223,876,99]
        S = ['bw','tg','fgf','aa']
        print(radixsort(L))
        print(radixSortString(S))
        
        
    except:
        print("error")
        
