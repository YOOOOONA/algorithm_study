# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:47:29 2019

@author: 융
"""
import itertools

def solution(numbers):#numbers에는 숫자로이루어진 문자열이 들어감...0을 어떻게 처리할 것인가?
    answer = 0
    #numbers를 받아서 조합을 만든다음 int로 바꾸고 배열에 중복성확인하고 넣은다음 소수면 냅두고 아니면 뺸다.
    arr=[]
    numbers_list=list(numbers)
    for i in range(1,len(numbers)+1):
        arr.extend((map(''.join, itertools.permutations(numbers_list,i))))

    arr=list(set(map(int,arr)))
    for i in arr:
        cnt=0
        if i<2:
            continue
        for j in range(1,i):
            if i%j==0:
                cnt+=1
                if(cnt>2):
                    break
        if cnt==1:
            answer+=1
    return answer
print(solution("011"))