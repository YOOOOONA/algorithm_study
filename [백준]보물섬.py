# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 23:48:12 2020

@author: 융
"""
#[백준]보물섬....이게 왜 bfs문제냐? 최단으로 가는 경로들 중 가장 긴 경로 찾는 거니까!
from collections import deque
from sys import stdin#이거 두줄 써야 런타임 에러 안
input = stdin.readline

n,m=map(int,input().split())
ocean=[list(input().split()) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(i,j):
    dq=deque()
    dq.append((i,j,0))
    visited[i][j]=1
    dist=0
    while dq:
        x,y,d=dq.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if nx<0 or nx>n or ny<0 or ny>m:
                continue
            if visited[nx][ny]==0 and ocean[nx][ny]=='L':
                dq.append([nx,ny,d+1])
                dist=max(dist,d+1)
                visited[nx][ny]=1
    return dist#최장거리

answer=0
for i in range(n):
    for j in range(m):
        if ocean[i][j]=='L':
            visited=[[0]*m for _ in range(n)]#이게 중요함..L만 조사하되 L나올때마다 조사하는 거라..
            answer=max(answer,bfs(i,j))
print(answer)