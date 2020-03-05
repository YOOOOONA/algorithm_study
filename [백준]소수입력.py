# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 23:37:21 2020

@author: 융
"""

#[백준]소수입력
n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in li:
    f=True
    if i<=1:continue
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        cnt+=1
print(cnt)
    