# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:29:13 2019

@author: 융
"""
'''
입력:
4 6
101111
101010
101011
111011 첫째칸에서 마지막칸까지 가는 최단 경로 지나는 칸 개수

출력:15
'''
'''
n,m = map(int,input().split())
matrix= [list(input().split()) for _ in range(n)]#nxm 매트릭스
def dfs(start, matrix, footprints):
    footprints=[start]
'''
#이거 다 적용시키기 위해서 N+2, M+2길이 만큼의 매트릭스 생성함 테두리는 0
di = [0,0,-1,1]
dj = [-1,1,0,0]

def bfs(v):
    q=[v]
    level=0
    state=False
    while q:
        level+=1
        for _ in range(len(q)):
            v=q.pop(0)
            if v==(n,m):
                state=True#n,m도착하면 state 변경 후
                break#빠져나가
            if matrix[v[0]][v[1]]=='1':
                matrix[v[0]][v[1]]='0'
                for a in range(4):
                    if matrix[v[0]+di[a]][v[1]+dj[a]]=='1':
                        q.append((v[0]+di[a], v[1]+dj[a]))
        if state:
            break
    print(level)
        

n,m = map(int,input().split())
matrix= [['0']*(m+2)]+[list('0'+input()+'0') for _ in range(n)]+[['0']*(m+2)]#nxm 매트릭스
bfs((1,1))














