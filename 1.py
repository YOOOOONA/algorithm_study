<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:42:52 2020

@author: 융
"""

for i in range(2):
    for j in range(2):
        mat = [[0 for _ in range(2)] for _ in range(2)] 
        (mat[1])[1]=9
        while True:
            print('before',i,j,mat)
            mat[i][j] +=1
            print('after',i,j,mat)
            if mat[i][j] == 2:
                
                break
            i=(i+1)%2
            j=(j+1)%2
            
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 12:42:52 2020

@author: 융
"""

for i in range(2):
    for j in range(2):
        mat = [[0 for _ in range(2)] for _ in range(2)] 
        (mat[1])[1]=9
        while True:
            print('before',i,j,mat)
            mat[i][j] +=1
            print('after',i,j,mat)
            if mat[i][j] == 2:
                
                break
            i=(i+1)%2
            j=(j+1)%2
            
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
        