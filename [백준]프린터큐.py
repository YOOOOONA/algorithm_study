# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:04:34 2020

@author: 융
"""

#1.가장 앞에 있는 문서의 ‘중요도’를 확인
#2.나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄

#현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것
#import sys
#input = sys.stdin.readline()

def solution(where,prior):
    cnt = 0
    while True:
        if prior[0] == max(prior):
            cnt += 1#맨앞에 값이 max일때만 프린트 되고 이때만 카운트해야됨
            if where[0] == 1:
                return cnt
            else:
                prior.pop(0)
                where.pop(0)
        else:
            prior.append(prior[0])
            where.append(where[0])
            prior.pop(0)
            where.pop(0)
    
        

T = int(input())
ans = []
for _ in range(T):
    
    N,M = map(int,input().split())#N=100이하의 문서 개수, M=N미만의 목표값의 현재 위치
    prior = list(map(int,input().split()))#1이상9이하의 중요도 N개 주어짐
    where = [0] * N
    where[M] = 1
    ans.append(solution(where,prior))
for i in ans:
    print(i)
