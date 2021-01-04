# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 22:39:33 2020

@author: 융
"""

def solution(op,num,que):
    if op == 'I':
        que.append(num)
        que.sort(reverse=True)
    elif op == 'D':
        if num == -1: que.pop()
        elif num == 1: que.pop(0)
    return que

T = int(input())
for _ in range(T):
    N = int(input())
    que = []
    for _ in range(N):
        op,num = list(map(int,input().split()))
        que = solution(op,num,que)
    print(max(que),min(que))
