# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:21:57 2020

@author: 융
"""
import copy
#이미 최소경로를 알려줌...더이상의 최소는 없다. 
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
graph_cp=copy.deepcopy(graph)
d=[[100000000]*N for _ in range(N)]
def fw(graph):
    
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if k==i or i==j or j==k:
                    continue
                elif graph[i][j]>graph[i][k]+graph[k][j]:
                    print("no",i,j)
                    return -1
                elif graph[i][j]
    print(graph)
#print(fw(graph))
fw(graph)                
'''
[[0, 6, 15, 2, 6], 
 [6, 0, 9, 8, 12], 
 [15, 9, 0, 16, 18], 
 [2, 8, 16, 0, 4], 
 [6, 12, 18, 4, 0]]
'''