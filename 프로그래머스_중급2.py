# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 01:58:26 2019

@author: 융
"""

#조이스틱 조작횟수
'''
AAAAA->JEROEN : 56번//A->N:13번,A->Z->M:13번   ,문자간 이동=문자열길이-1
AAA->JAN : 23번
'''
def solution(w):
    answer=0
    for i in w:
        print(i,type(i))
        if i=='A':
            print("answer",answer)
            continue
        elif i>'A' and i<='M':
            answer+=ord(i)-ord('A')
            print("answer",answer)
        elif i>'M' and i<='Z':
            answer+=1+ord('Z')-ord(i)
            print("answer",answer)
        #만약 JJAAAAJ면 
        if w[2]
    answer+=(len(w)-1)
    return answer
print(solution('JEROEN'))