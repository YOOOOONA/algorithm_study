# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:35:30 2020

@author: 융
"""

T=int(input())
for _ in range(T):
    N=int(input())
    mat=[]
    wall=[[0*i for i in range(N)] for _ in range(N)]
    mcnt=0
    #mat 입력받으면서 테두리 코어 개수 세기
    for i in range(N):
        if i==0 or i==N-1:
            li=list(map(int,input().split()))
            mat.extend(li)
            wall[i]=li
            #mcnt+=sum(li)
        else:
            li=list(map(int,input().split()))
            mat.extend(li)
            wall[i][0]=mat[i][0]
            wall[i][N-1]=mat[i][N-1]
            #mcnt+=li[0]+li[N-1]
    for i in range(N):
        for j in range(N):
            if mat[]:
def dfs(cores,)