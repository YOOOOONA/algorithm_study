# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 00:23:56 2019

@author: 융
"""
def solution(d, budget):#d는 배열, budget은 예산, answer는 지원가능한부서개수
    answer = 0
    d.sort(reverse=True)#큰것부터
    for i in range(len(d)):
        mon = sum(d[i:])
        print("돈",mon)
        if mon <= budget:
            answer = len(d)-i
            break
    return answer
print("답은",solution([1,3,2,5,4], 9))
