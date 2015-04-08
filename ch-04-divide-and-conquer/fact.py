#!ipython3

def fact (n):
    '''階乗関数'''
    if n == 0:
        return 1
    else:
        return n*fact (n-1)
    
def fact1(n,a = 1):
    if n == 0:
        return a
    else:
        return fact1(n-1,n*a)
