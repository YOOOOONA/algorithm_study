# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:57:38 2020

@author: 융
"""
from collections import deque

N=int(input())
mat=[list(map(int,input())) for _ in range(N)]
visited=[[0 for _ in range(N)] for _ in range(N)]
r=[0,0,1,-1]
c=[1,-1,0,0]
apt_li=[]

def bfs(i,j):
    apt_cnt=0
    dq=deque()
    dq.append([i,j])
    while dq:
        x,y=dq.popleft()
        visited[x][y]=1
        #print(x,y)
        apt_cnt+=1
        for k in range(4):
            dx=x+r[k]
            dy=y+c[k]
            if 0>dx or dx>=N or 0>dy or dy>=N: continue
            if visited[dx][dy]==0 and mat[dx][dy]==1:
                visited[dx][dy]=1
                dq.append([dx,dy])
    apt_li.append(apt_cnt)
    return 1#길찾으면 1,아니면 0 리턴..하려고 했는데 생각해 보니 i,j만으로도 이미 1개 아파트 있는 것

cnt=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0 and mat[i][j]==1:
            cnt+=bfs(i,j)
print(cnt)
apt_li.sort()
for a in apt_li:
    print(a)
#print("단지수:",cnt,"아파트 수:",apt_li)
            