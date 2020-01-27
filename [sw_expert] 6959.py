# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:56:27 2020

@author: 융
"""

T=int(input())

for j in range(T):
    N=input()
    #l=len(N)
    winner=['B','A']
    cnt=0
    while(len(N)>1):
        a=int(N[0])+int(N[1])
        if len(N)>=2:
            N=str(a)+N[2:]
        else:
            N=str(a)
        cnt+=1        
        #print("??",N,print(winner[cnt%2]),end=' ')
    print("#%d %s" %(j,winner[cnt%2]))