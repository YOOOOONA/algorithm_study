# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:48:33 2019

@author: 융
"""
#유효성 불통
def solution(s):#문자열 s, 짝지어 제거 되면 1 아니면 0 리턴
    answer = 0
    while(True):
        ch = 1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                s=s[:i]+s[i+2:]#어렵게 가지말고 그냥 문자열 잘라붙이면 되네!
                ch-=1
                break
        if len(s)==0:
            answer=1
            return answer
        elif ch==1:
            return answer
        
#유효성 통과
def solution1(s):
    answer_list=[]
    s=list(s)
    idx=0
    while(idx!=len(s)):
        answer_list.append(s[idx])
        idx+=1
        if len(answer_list)>1:
            if (answer_list[-1]==answer_list[-2]):
                answer_list.pop()
                answer_list.pop()      
    if len(answer_list)==0:
        return 1
    else:
        return 0

print(solution('cdcd'))