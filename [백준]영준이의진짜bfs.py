# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:48:03 2020

@author: 융
"""

#bfs
#bfs로 1번부터 돌았을 때 지나는 총 간선 개수 리턴


import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def makeGraph(n,edges):
    
    #1 1 2 
    #그래프 만들기
    graph = dict()
    print('\n',edges)
    for i in range(1,n):
        if edges[i-1] not in graph:
            graph[edges[i-1]] = [i+1,]
        else:
            graph[edges[i-1]].append(i+1)
    print('graph:',graph)   
    return graph

def lca(n,graph):
    #노드가 n개일 때 각 노드의 부모노드찾기
    #1은 부모노드가 없어
    for i in range(2,n+1):
        for sub in graph:
            if i in 





def bfs(n,graph):
    #일단 pop하고 append할 때 횟수 세서 몇개모자라는지 확인
    ans = 0
    q = [1,]
    while q:
        out = q.pop(0)
        ans += 1
        if out in graph:
            q.extend(graph[out])
            ans += len(graph[out])
        
    return ans

def solution(n,edges):
    graph = makeGraph(n,edges)
    return bfs(n,graph)

T = int(input())
for tc in range(T):
    n = int(input())
    edges = list(map(int, input().split()))
    ans = solution(n,edges)
    print("#{} {}".format(tc+1, ans))
'''
d = dict()
d[1]=[1,2,3]
print(d)
if 3 in d[1]:
    d[1].append(4)
print(d)
'''