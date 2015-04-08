#!env ipython3

L =[13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]

def find_max_crossing_simple(L):
    size = len(L)
    mid = int(size/2)
    max_left = 0
    max_right = 0
    left_sum = - float("inf")
    SUM_L = 0
    for i in range(mid,-1,-1):
        SUM_L += L[i]
        if SUM_L > left_sum:
            left_sum = SUM_L
            max_left = i
    SUM_R = 0
    right_sum = - float("inf")
    for j in range(mid + 1 ,size):
        SUM_R += L[j]
        if SUM_R > right_sum :
            right_sum = SUM_R
            max_right  = j
    return (max_left ,max_right,left_sum + right_sum)

def find_max_crossing_subarray (L,low,mid,high):
    max_left = 0
    max_right = 0
    left_sum = - float ('inf')
    SUM = 0
    for i in range (mid,low-1,-1):
        SUM += L [i]
        if SUM > left_sum:
            left_sum = SUM
            max_left = i
    right_sum = - float ('inf')
    SUM_R = 0
    for j in range (mid + 1 , high):
        SUM_R += L [j]
        if SUM_R > right_sum:
            right_sum =  SUM_R
            max_right = j        
    return (max_left, max_right , left_sum + right_sum)


def find_maximum_subarray (L,low,high):
    '''分割統治アルゴリズム：リストを左右に分け最大部分配列を決定
    中央値より小さい場合、中央値をまたぐ場合、中央値より大きい場合と３通りいo'''
    mid =int ((low + high) /2)
    if  high == low:
        return (low,high,L [low])
    l_low,l_high,l_sum = find_maximum_subarray (L ,low,mid)
    r_low,r_high,r_sum = find_maximum_subarray (L ,mid + 1,high)
    c_low,c_high,c_sum = find_max_crossing_subarray (L,low,mid,high)
    if l_sum >= r_sum and l_sum >= c_sum:
        return [l_low,l_high,l_sum]
    elif r_sum >= l_sum and r_sum >= c_sum:
        return [r_low,r_high,r_sum]
    else:
        return [c_low,c_high,c_sum]
        
