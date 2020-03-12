# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 00:38:47 2020

@author: 융
"""
#세개 더했을 때 소수가 되는 경우의 수 출력
def solution(nums):
    #서로다른 세개의 수 뽑는 경우의 수 만들기
    li=[]
    answer=0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                li.append(nums[i]+nums[j]+nums[k])
                
    #그 수들의 합이 소수일 경우 카운트하기
    for num in li:
        flag=True
        for i in range(2,num-1):
            if num%i==0:
                flag=False
                break
        if flag==True:
            answer+=1
                
    return answer
print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))