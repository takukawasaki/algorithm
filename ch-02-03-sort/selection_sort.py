#!ipython3
def selection_sort (L):
    """リストをまずL[0] L[1:]二つにわけ一方の最小値を探しL[0]に	入れ替え次はL[1],L[2:]以降と 繰り返す """
    size = len(L)
    for i in range (size):
        mins = L [i]
        for j in range (i + 1, size):
            if L [j]  < mins:
                mins = L [j]
                L [j] = L [i]
            L [i] = mins
    return L       
