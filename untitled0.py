# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:29:27 2020

@author: 융
"""

def solution(M,N,x,y):
    ans = 0
    while(True):
        x = (x+1)%M if (x+1)%M != 0 else M , y = (y+1)%N if (y+1)%N != 0 else N 
        if x == M and y == N:
            return ans
        if x > M or y
T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    print(solution(M,N,x,y))
    
    
M=3, N=4
1,1
2,2
3,3
1,4
2,1
3,2
1,3
