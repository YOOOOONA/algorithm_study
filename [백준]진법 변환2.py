# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 13:28:47 2020

@author: 융
"""

N,B=map(int,input().split())
ans=''
if B<=10:
    while N>0:
        ans=str(N%B)+ans
        N=N//B
elif 10<B<=36:
    while N>0:
        B_alph=N%B
        if B_alph >= 10:
            B_alph=chr(ord('A')+(B_alph-10))
        ans=str(B_alph)+ans
        N=N//B
print(ans)
'''
print(chr(ord('a')+10))
'''