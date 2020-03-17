# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:47:07 2020

@author: 융
"""

#dfs
from collections import deque
#한방향으로 쭉 익는 것이 아니라 퍼지면서 익는 것이라 bfs로만 풀 수 있음
'''
M,N=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(N)]
visited = mat.copy()
r = [0,0,-1,1]
c = [-1,1,0,0]
def dfs(mat,i,j):
    stack = deque()
    stack.append([i,j])
    while stack:
        x,y=stack.pop()
        visited[x][y] = 1
        for i in range(4):
            dx=x+r[i]
            dy=y+c[i]
            if 0<=dx<N and 0<=dy<M and mat[dx][dy]!=-1 and visited[dx][dy]==0:
                stack.append([dx,dy])
                visited[dx][dy] = 1
        
    return mat

for i in range(N):
    for j in range(M):
        if mat[i][j] == 1 and visited[i][j] == 0:
            mat = dfs(mat,i,j)
        if mat[i][j] == -1:
if 0 in mat:
'''
from collections import deque
def bfs(M, N, box):
    # 좌우상하
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    days = -1

    while ripe:
        days += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    ripe.append([nx, ny])

    for b in box:
        if 0 in b:
            return -1
    return days


M, N = map(int, r().split())
box, ripe = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1:
            ripe.append([i, j])
    box.append(row)


print(bfs(M, N, box))
            