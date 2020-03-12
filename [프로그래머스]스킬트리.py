# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:45:13 2020

@author: 융
"""

def solution(skill, skill_trees):
    
    cnt=0
    for w in skill_trees:
        li=[]
        print(w)
        for s in skill:
            if s in w:
                li.append(w.index(s))
            else:
                li.append(9999)
        li_s=li.copy()
        li_s.sort()
        if li_s==li:
            cnt+=1
    return cnt
print(solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"]))
'''
li=[1,2,3,2,1]
li_s=li.copy()
li_s.sort()
print(li,li_s)
'''