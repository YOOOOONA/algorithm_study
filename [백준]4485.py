# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 00:20:58 2021

@author: 융
"""
#다익스트라 는 적은거 갱신하는거 까지가 다익스트라임... dp를 사용하는것...!
from heapq import heappush,heappop
import sys
import copy
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

d = [(0,1),(1,0),(-1,0),(0,-1)]

def solve(mat,C):
    # ansLi = []
    visited = [[False for _ in range(C)] for _ in range(C)]
    dp = [[100000000 for _ in range(C)] for _ in range(C)]
    dp[0][0] = mat[0][0]
    q = []
    heappush(q,[mat[0][0],[0,0]])
    while q:
        pr,loc = heappop(q)
        for i in range(4):
            #우,하,상 만 고려하면 됨
            nxI, nxJ = loc[0]+d[i][0],loc[1]+d[i][1]
            if 0<=nxI<C and 0<=nxJ<C and not visited[nxI][nxJ]:
                visited[nxI][nxJ] = True
                dp[nxI][nxJ] = min(dp[nxI][nxJ],dp[loc[0]][loc[1]] + mat[nxI][nxJ])
                heappush(q,[dp[nxI][nxJ],[nxI, nxJ]])
    return dp[C-1][C-1]
t = 1    
while(True):
    C = int(input())
    if not C: break
    mat = [list(map(int,input().split())) for _ in range(C)]
    ans = solve(mat,C)
    print("Problem {}: {}".format(t,ans))
    t+=1