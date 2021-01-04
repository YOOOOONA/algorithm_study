# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 23:14:28 2020

@author: 융
"""
'''
#팰린드롬, 이효리 거꾸로해도 이효리 개수 구하기
def binary_search(low,high,target,li):
    mid = (low+high)//2
    if target < li[mid]:
        binary_search(low,mid-1,target,li)
    elif target > li[mid]:
        binary_search(mid+1,high,target,li)
    elif target == li[mid]:
        return mid
    
def solution(n,m):
    for l in range(len(n),len(m)+1):
        #자릿수 l이 홀수일 때
        if l%2==1:
            for i in range(l//2):
                if m 
        #자릿수 l이 짝수일 때
    return answer
solution(1,100)#1이상 100이하에서 18개있음 1,2,3,4,5,6,7,8,9,11,22,33,,99
solution(100,300)#20     101,111,121,131,,,202,,,292,,303,,909,,999
solution(1000,3000)

def solution(v):
    x = []
    y = []
    for i in v:
        _x = i[0]
        if _x not in x: x.append(_x)
        else: x.remove(_x)
        _y = i[1]
        if _y not in y: y.append(_y)
        else: y.remove(_y)
    answer = [x[0],y[0]]
    return answer
print(solution([[1,4],[3,4],[3,10]]))#[1,10]  네점으로 직사각형만들때 필요한 나머지 한 점
print(solution([[1,1],[2,2],[1,2]]))
'''
def solution(n,m):
    dp = [[]]*(len(str(m))+1)
    dp[1]=[1,2,3,4,5,6,7,8,9]
    for i in range(len(str(n)),len(str(m))+1):
        if i==1: continue
        for j in range(2,i+1):
            for k in dp[j-1]:
                dp[j].append([int(str(a)+str(k)+str(a)) for a in range(10)])
                #print(dp,'\n')
    return dp
print(solution(1,1000))