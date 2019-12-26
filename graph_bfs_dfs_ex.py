# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 12:16:27 2019

@author: 융
"""

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D', 'G'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
def bfs(graph,start):
    #visit=[]
    visit={}
    queue=[]
    queue.append(start)
    while(queue):
        node=queue.pop(0)        
        if node not in visit:
            #visit.append(node)
            visit[node]=True
            queue.extend(graph[node])
    return visit

def dfs(graph,start):
    visit=[]
    stack=[]
    stack.append(start)
    while(stack):
        node=stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

from queue import Queue
def bfs2(graph,start):
    visit=set()#딕셔너리나 셋으로 관리해야됨.중복방지하려고
    q=Queue()#파이썬 리스트는 스택과 유사하지만 큐랑은 다른구조임 그래서 큐는 임포트해서 쓰는게 시간 아낌
    q.put(start)
    
    while(q.qsize()>0):
        node=q.get()
        #print(node)
        if node not in visit:
            visit.add(node)
            for nodeNext in graph[node]:
                q.put(nodeNext)
    return visit
            
print(bfs2(graph,'B'))