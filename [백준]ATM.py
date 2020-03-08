# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 16:33:16 2020

@author: 융
"""

N=int(input())
li=list(map(int,input().split()))
li.sort(reverse=False)
li.append(0)
print(li)
ans=0
for i in range(N):
    ans+=sum(li[:i+1])
        
print(ans)