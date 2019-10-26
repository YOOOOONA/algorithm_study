# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 02:41:26 2019

@author: 융
"""
'''
#import sys
from collections import deque
#input=sys.stdin.readline

def solve():
    while q:
        cur = q.popleft()
        if cur ==k:
            return visit[cur]
        nextPos(cur - 1,cur)
        nextPos(cur + 1,cur)
        nextPos(cur * 2,cur)
        
def nextPos(nex, cur):
    #nex 지점이 범위 내에 있고
    #한번도 방문하지 않았거나, 최소 time으로 해당 방을 방문한 경우
    if maxSize>nex>=0 and (0==visit[nex] or visit[cur]+1<visit[nex]):
        visit[nex]=visit[cur]+1
        q.append(nex)
        
if __name__=="__main__":
    n,k=map(int, input().split())
    maxSize=100001
    visit=[0]*maxSize
    q=deque([n])
    print(solve())
    
'''
#import sys
#input=sys.stdin.readline

def bfs(v):
    visited=[False]*100001
    q=[v]
    cnt=0
    state = False
    
    while q:
        for _ in range(len(q)):
            v=q.pop(0)
            if not(visited[v]):
                if v==K:
                    state = True
                    break
                if v-1>=0:
                    q.append(v+1)
                if v+1<=100000:
                    q.append(v+1)
                if v*2<=100000:
                    q.append(v*2)
        if state:
             print(cnt)
             break
        cnt+=1
N,K=map(int,input().split())
bfs(N)
                    
                    
                    
                    
                    




















