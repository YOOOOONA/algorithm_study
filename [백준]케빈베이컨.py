# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:07:50 2020

@author: 융
"""
'''
from collections import deque
graph={}
M,N=map(int,input().split())
con=[list(map(int,input().split())) for _ in range(N)]
for i in range(1,M+1):
    a=[]
    for n in con:
        if i in n:
            n.remove(i)
            a.extend(n)
            n.append(i)
    graph[i]=set(a)
print(graph)


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    print("큐:",queue)
    result = []
    minl=1000000
    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
            minl=min(minl,len(path))
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
        print("큐:",queue)
        
    return minl
leng=[[0 for _ in range(M+1)] for _ in range(M+1)]
for i in range(1,M+1):
    for j in range(1,M+1):
        leng[i][j]=bfs_paths(graph,i,j)
        print(bfs_paths(graph,i,j))
print(leng)
dic={}

for i in range(1,M+1):
    dic[i]=0
    for j in range(1,M+1):
        dic[i]+=leng[i][j]
print("dic:",dic)
minidx=1
for i in range(1,M):
    if dic[i]<dic[minidx]:
        minidx=i
print("최소인덱스",minidx)
'''
from collections import deque
graph={}
M,N=map(int,input().split())
con=[list(map(int,input().split())) for _ in range(N)]
for i in range(1,M+1):
    a=[]
    for n in con:
        if i in n:
            n.remove(i)
            a.extend(n)
            n.append(i)
    graph[i]=set(a)
#print(graph)


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    #print("큐:",queue)
    result = []
    minl=60000
    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
            minl=min(minl,len(path))
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
        #print("큐:",queue)
        
    return minl
leng=[[0 for _ in range(M+1)] for _ in range(M+1)]
for i in range(1,M+1):
    for j in range(i+1,M+1):
        x=bfs_paths(graph,i,j)
        leng[i][j]=x
        leng[j][i]=x
        #print(bfs_paths(graph,i,j))
#print(leng)
dic={}

for i in range(1,M+1):
    dic[i]=0
    for j in range(1,M+1):
        dic[i]+=leng[i][j]
#print("dic:",dic)
minidx=1
for i in range(1,M):
    if dic[i]<dic[minidx]:
        minidx=i
print(minidx)

###########################남의코드...내코드는 시간초과 뜸

#입력
N, M = map(int, input().split())
friend_map = [[N for _ in range(N)] for _ in range(N)]

for _ in range(M):
    friend_A, friend_B = map(int, input().split())
    friend_map[friend_A-1][friend_B-1] = 1
    friend_map[friend_B-1][friend_A-1] = 1


#플로이드-워셜 알고리즘#################
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if i == j:
                friend_map[i][j] = 0 #자기 자신과는 친구가 되지 못한다
            else:
                friend_map[i][j] = min(friend_map[i][j],
                                       friend_map[i][k] + friend_map[k][j])


#출력
bacon = []
for row in friend_map:
    bacon.append(sum(row))
print(bacon.index(min(bacon)) + 1)