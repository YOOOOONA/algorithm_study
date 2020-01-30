# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 01:09:05 2020

@author: 융
"""
'''
input
2
banana bana
asakusa sa	//Test Case의 개수
//A=”banana”, B=”bana”
//A=”asakusa”, B=”sa”


output
#1 3
#2 5	//Test Case 1번의 답
//Test Case 2번의 답
'''
T=int(input())
for i in range(T):
    A,B=input().split()
    cnt=A.count(B)
    print("#%d %d" %(i+1,(len(A)-cnt*(len(B)-1))))    