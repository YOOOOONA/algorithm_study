# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 03:27:12 2020

@author: 융
"""
import math
def solution(n, words):
    dic={}
    for w in words:
        dic[w]=0
    for i in range(len(words)):
        if dic[words[i]]==0:
            dic[words[i]]+=1
        else:
            ans=i
            print(ans)
            break
        if i==len(words)-1:
            return [0,0]
            
        if words[i][-1]==words[i+1][0]:
            continue
        else:
            ans=i+1
            break
    answer=[ans%n+1,math.ceil((ans+1)/n)] 
    return answer