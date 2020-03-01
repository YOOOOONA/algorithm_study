# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 01:37:58 2020

@author: 융
"""
#[백준]바이러스 bfs,dfs

from collections import deque
r=[0,0,1,-1]
c=[1,-1,0,0]

C=int(input())#컴퓨터 대수
l=int(input())#연결선 개수
dq1=[]
graph=[[0]*(C+1) for _ in range(C+1)]

visited=[[0]*(C+1) for _ in range(C+1)]
def bfs(graph,start):
    global visited
    dq=deque()
    dq.append(start)
    visited=[]
    
    while dq:
        nex=dq.popleft()
        visited.append(nex)
        for i in range(1,C+1):
            if graph[nex][i] and i not in visited and i not in dq:
                dq.append(i)
    print(visited)
    return len(visited)-1


for _ in range(l):
    i,j=map(int,input().split())
    graph[i][j]=1
    graph[j][i]=1




i=1
#print(bfs(i,j))
#dq1=set(dq1)
print(bfs(graph,1))