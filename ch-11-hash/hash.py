#!ipython3

import numpy as np
from numpy import random
import string


Alp = string.ascii_lowercase[:26]

D = {i: j for i,j in zip(Alp,[j for j in range(26)]) }

L = [[i , j] for i , j in  zip(Alp,range(26))]

AtoZ = [chr(i) for i in range(ord('A'),ord('Z')+3)]


def direct_address_search(T,k):
    for i in range(len(T)):
        for j in T[i][0]:
            if j == k:
                return T[i][1]
            else:
                pass

            
