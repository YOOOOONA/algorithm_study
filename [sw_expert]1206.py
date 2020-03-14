# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:50:36 2020

@author: 융
"""

T=10
for t in range(T):
    l=int(input())
    answer=0
    apt=list(map(int,input().split()))
    for i in range(2,l-2):
        max_h=max(max(apt[i-1],apt[i-2]),max(apt[i+1],apt[i+2]))
        if apt[i]>max_h:
            answer+=apt[i]-max_h
    print("#%d %d",t+1,answer)