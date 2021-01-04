# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:22:51 2020

@author: 융
"""
'''
import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())
adj = [list(map(int,input().split())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj[i][k] and adj[k][j]: 
                adj[i][j] = 1
            
for i in range(N):
    print(*adj[i])
'''
#a =     +   
#print(a/144)
b = (17 *   3.58   +   19   *   3.53)/(17+19)
print(b)
b = (15   *   3.58   +   15   *  2.6   +   2   *   3.3)/(32)
print(b)

b = (18   *   3.11   +   18   *   3.28   +   3   *   3.0 )/39
print(b)
b = (13   *   3.39   +   3   *   4.0   +   15   *   3.44   +   3   *   4.0)/34
print(b)