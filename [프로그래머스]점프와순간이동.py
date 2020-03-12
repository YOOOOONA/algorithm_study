# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:52:46 2020

@author: 융
"""
#k칸 앞으로 이동 or 현재까지온거리*2만큼 순간이동 가능. k칸 이동은 k만큼 건전지 닳아. 
#N거리에 가려고 해.최대한 순간이동 많이 해서
#사용해야되는 최소건전지양 리턴
def sol(n,answer):
    if n==1 or n==2:
        return answer#####
    else:
        if n%2==1:
            return sol((n-1)//2,answer+1)######꼭 리턴을 써줘야지
        else:
            return sol(n//2,answer)#####
def solution(n):
    answer=1
    return sol(n,answer)
print(solution(5))
print(solution(6))
print(solution(5000))