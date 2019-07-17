# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 16:39:17 2019

@author: 융
"""
t=input()
t=int(t)
for j in range(t):
    time=0
    n,p=input().split(" ")
    s=input().split(" ")
    n=int(n)
    p=int(p)
    for i in range(n):
            s[i]=int(s[i])
    if n==int(p):
        
        for i in s:
            time+=(max(s)-i)
            
    else:
        resultdif=10000000
        resulttime=0
        s_s=sorted(s)
        
        for k in range(n-p+1):
            subset=[]
            time=0
            for g in range(k,k+p):
                subset.append(s_s[g])
            dif= subset[-1]-subset[0]
            
            if(resultdif>dif):
                resultdif=dif
                for i in subset:
                    time+=(subset[-1]-i)
                resulttime=time
                
        time=resulttime
        
    print("Case #",j+1,":",time)
