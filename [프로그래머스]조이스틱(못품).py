# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:37:11 2020

@author: 융
"""

def solution(name):
    answer = -1
    i=0
    flag=True
    pl=1#방향 키
    n_A=[]
    for n in name:
        if n=='A':
            n_A.append(0)
        elif 'A' < n <= 'M':
            n_A.append(n - 'A')
        elif 'N' <= n <= 'Z':
            n_A.append('Z'- n + 1)
    for k in range(len(name)):
        if name[k]==0:
            
   [1,1,0,1,0]=>6
   [1,1,1,0,0,1]=>8
   [1,1,0,0,1,0,0]=>7
   [1.1.0,0,1,1,1]=?10
   [1,1,0,0,1,0,0,0,0]=>7
   [1,1,0,0,1,0,0,0,1]=>10