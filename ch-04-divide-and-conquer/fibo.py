#!ipython3

def fibo (n):
    '''フィボナッチ関数'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo (n-1) + fibo (n-2)

def fibo_recursive(n):
    '''フィボナッチ関数再帰'''
    return fibo_iter(1,0,n)

def fibo_iter(a,b,n):
    '''フィボナッチ関数再帰補助'''
    if n == 0:
        return b
    else:
        return fibo_iter(a+b , a ,n-1) 

    
