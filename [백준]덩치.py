<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:25:58 2020

@author: 융
"""
#브루트포스 완전탐색
def solution(li):
    ans = []
    for i in range(len(li)):
        x,y = li[i]
        cnt = len(li)+1
        for j in range(0,len(li)):
            if x >= li[j][0] or y >= li[j][1]:
                cnt -= 1
        print(cnt, end = ' ')
    
N= int(input())
li = []
for _ in range(N):
    x,y = map(int,input().split())
    li.append([x,y])# 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
=======
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:25:58 2020

@author: 융
"""
#브루트포스 완전탐색
def solution(li):
    ans = []
    for i in range(len(li)):
        x,y = li[i]
        cnt = len(li)+1
        for j in range(0,len(li)):
            if x >= li[j][0] or y >= li[j][1]:
                cnt -= 1
        print(cnt, end = ' ')
    
N= int(input())
li = []
for _ in range(N):
    x,y = map(int,input().split())
    li.append([x,y])# 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
solution(li)