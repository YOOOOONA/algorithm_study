# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 00:43:54 2020

@author: 융
"""

def solution(N,road,K):
    #visited = [False for _ in range(N+1)]
    #pdb.set_trace()
    costs = [float('inf') for _ in range(N+1)]
    costs[1] = 0
    parents = [1]
    
    while(parents):
        parent = parents.pop(0)
        
        #visited[parent] = True
        
        for a,b,cost in road:
            if a == parent or b == parent :
                target = b if a == parent else a
                if costs[target] > costs[parent] + cost:
                    costs[target] = costs[parent] + cost
                    parents.append(target)
    return sum(1 for c in costs if c <= K)#모든 정점까지의 최단경로의 비용을 다 담아서 기준 안넘기는 애들 카운트