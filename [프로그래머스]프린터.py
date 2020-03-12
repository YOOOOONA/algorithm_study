# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 19:30:09 2020

@author: 융
"""

def solution(p, l):
    ans=0
    while(True):
        ll=len(p)
        m=max(p)
        v=p.pop(0)
        if m==v:#맨앞에꺼가 맥스일 때 
            ans+=1
            if l==0:                 
                break
            else:
                l-=1
        else:#아닐 때            
            if l==0:
                l=ll-1
            else:
                l-=1
            p.append(v)
    return ans
print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))