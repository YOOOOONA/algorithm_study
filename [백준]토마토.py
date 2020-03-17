# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:47:07 2020

@author: 융
"""

#dfs
from collections import deque
#한방향으로 쭉 익는 것이 아니라 퍼지면서 익는 것이라 bfs로만 풀 수 있음
def show(mat,N,M):
    for i in range(N):
        print(mat[i])
    print("\n")
M,N=map(int,input().split())
mat=[list(map(int,input().split())) for _ in range(N)]
#visited = mat.copy()

def select_max(mat,N):
    mm=0
    for i in range(0,N):
        m= max(mat[i])
        mm = max(mm,m)
    return mm

r = [0,0,-1,1]
c = [-1,1,0,0]
def bfs(mat,queue):    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            dx=x+r[i]
            dy=y+c[i]
            if 0<=dx<N and 0<=dy<M and mat[dx][dy]!=-1:
                #print('좌표',dx,',',dy)
                if mat[dx][dy] !=0:
                    mat[dx][dy] =min(mat[dx][dy], mat[x][y] + 1)
                    #print("큐",queue)
                else:
                    queue.append([dx,dy])
                    mat[dx][dy] = mat[x][y] + 1
                show(mat,N,M)
    for m in mat:
        if 0 in m:
            #print("no answ")
            return -1
    show(mat,N,M)
    answ=select_max(mat,N)-1
    #print(answ)
    return answ 
queue = deque()
for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            #print(bfs(mat,i,j)) 이게 아니고
            queue.append([i,j])#1인 애들 모두 큐에 넣고 bfs한번만 함
print(bfs(mat,queue))
#print("답은",select_max(bfs(mat,queue),N)-1)
