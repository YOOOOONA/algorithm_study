import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
#다익스트라
from heapq import heappush,heappop
n = int(input())#도시개수
m = int(input())#버스개수
#[[start,end,cost]]
buses = [[] for _ in range(n+1)]#[list(map(int,input().split())) for _ in range(m)]
for i in range(m):
    s,e,c = map(int,input().split())
    buses[s].append([c,e])
info = list(map(int,input().split()))#start,end

def solution(info,buses):
    start,end = info

    q=[]
    mincost = [int(1e9) for _ in range(n+1)]
    mincost[start] = 0
    heappush(q,[0,start])
    while q:
        cost,pos = heappop(q)
        for c,p in buses[pos]:
            if cost + c < mincost[p]:
                mincost[p] = cost + c
                heappush(q,[cost + c, p])
    
    return mincost[end]
print(solution(info,buses))