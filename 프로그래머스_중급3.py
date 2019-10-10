# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:18:17 2019

@author: 융
"""

#[1,3,5,7,11]의 최소공배수찾기=11의 배수 11*1, 11*2,,,를 나머지수들로 다 나눠보고 모두 다 나머지가 0일떄 채택
def solution(arr):
    answer=0
    i=0
    arr=sorted(arr,reverse=True)
    while(True):
       i+=1
       com = arr[0]*i
       for j in range(1,len(arr)):
           if(com%arr[j]!=0):
               break
           if(j==len(arr)-1 and com%arr[j]==0):
               answer=com
           
       if answer!=0:
           break
    return answer
print(solution([2,6,8,14]))