#!ipython3


def counting_sort(L):
    size = len(L)
    k = max(L)
    B = []
    C = [0 for i in range(k + 1)]
    
    for j in range(size):
        C[L[j]] += 1


    for i in range(len(C)):
        while C[i] != 0:
            B.append(i)
            C[i] -= 1
    
    return L


if __name__== '__main__':
    try:
        L = [2,5,3,0,2,3,0,3,100]
        L = counting_sort(L)
        print(L)
        
    except:
        print("error")
        
