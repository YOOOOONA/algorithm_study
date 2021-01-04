# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:37:22 2020

@author: 융
"""
'''
import sys
input = sys.stdin.readline()


MAX = 100000#부모노드가 가질 수 없는 값 중 최솟값

def solution(tree,pair):#pair의 정점쌍의 가장 가까운 공통 조상을 출력
    print(tree,pair)
    for p in pair[1:]:
        e1 = tree[p[0]].copy()#[3,1]
        e2 = tree[p[1]].copy()#[11,5,2,1]
        
        p1, p2 = p[0], p[1]        
        while True:
            print("e쌍 p쌍:",e1,e2,'\n',p1,p2)
            if p1 == p2:
                print(p1)
                break
            elif p1 < p2:
                while p2<e2[0]:
                    e2.pop(0)
                p2 = e2.pop(0)
            elif p1 > p2:
                while p1 < e1[0]:
                    e1.pop(0)
                p1 = e1.pop(0)
                    
N = int(input())
tree = [[] for _ in range(N+1)]#[[연결된 두 정점],[연결된 두 정점],...,[연결된 두 정점]] 간선 14개 노드는 15개라서 1~15니까 16길이짜리 리스트 필요
for _ in range(N-1):
    p,c = map(int,input().split())#부모와 자식
    tree[p].append(c)
    tree[c].append(p)

for t in tree:
    t.sort(reverse=True)
     
M = int(input())#가장 가까운 공통 조상을 알고싶은 쌍의 개수 
pair = [list(map(int,input().split())) for _ in range(M)]#[[정점 쌍],[정점 쌍],...,[정점 쌍]]

solution(tree,pair)
'''
li = [ [-14,-5], [-20,15], [-18,-13], [-5,-3]]
#ll=[sorted(i) for i in li]
#sorted(li,key=lambda x:x in li)
li=[1,2,3,4,5]
li.sort()
print(li[-1:])
