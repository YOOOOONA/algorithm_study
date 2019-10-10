# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 00:30:26 2019

@author: 융
"""

def solution(s):#s는문자열->알파벳순서로 answer출력, 대문자는 소문자보다뒤에
    answer = ''
    s=sorted(s, reverse=True)
    '''
    for i in range(len(s)-1):
        a=s[i]
        for j in range(i,len(s)):
            if  a>s[j]:
                b=s[j]
                s[j]=a
                s[i]=b
    #대문자를 소문자 뒤로 보내기
    for i in range(len(s)):
        if s[i]>'a' and s[i]<'z' and i>0:
            Lar = s[0:i]
            Sma = s[i:]
            answer = Sma+Lar#문자열 합치는거 그냥 더하면 됨
            break
    '''
    for i in s:
        answer+=i
    return answer
print(solution("Zbcdefg"))