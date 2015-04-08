#!ipython3

import numpy as np
A = np.random.randn (2,2)
B = np.random.randn (2,2)


def square_matrix_mul (A,B):
    '''行列積を求める関数'''
    row = len (A)
    col = len (A [0])
    C = np.zeros ((row,col),dtype = np.float64)
    for i in range (0,row):
        for j in range (0 ,row):
            C [i] [j] = 0
            for k in range (0,row):
                C [i] [j] +=  A [i] [k] * B [k] [j]  
    return C
                
               





        
        






