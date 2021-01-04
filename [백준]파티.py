# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 00:43:10 2020

@author: 융
"""

import sys
from heapq import heappush, heappop
r = sys.stdin.readline
INF = 1e9

#heappush(큐,[우선순위,값])
#heappop=>우선순위 적은애가 젤 먼저 나옴
def dijkstra(mat,st):
    dist = [INF] * len(mat)
    dist[st] = 0
    
    q = []
    heappush(q,[0,st])
        
    while q:
        c_d, h = heappop(q)
        for end,we in mat[h]:
            next_d = dist[h] + we#현재지점 h까지의 가중치와 end까지 갈 가중치 더했을때 end지점에있는 가중치보다 작으면 갱신해주고 거기로 이동
            if next_d < dist[end]:
                dist[end] = next_d
                heappush(q,[we,end])
    return dist
    
n,m,x = map(int,r().split())
mat = [[] for _ in range(n+1)]
for _ in range(m):
    st,end,we = map(int,r().split())
    mat[st].append([end,we])
    
c = []
dist_h = dijkstra(mat,x)#x:파티위치에서 시작할때 각 지점까지의 최단 거리 리스트
 
for i in range(1,n+1):
    dist = dijkstra(mat,i)
    c.append(dist_h[i] + dist[x])#x to i + i to x
print(max(x))