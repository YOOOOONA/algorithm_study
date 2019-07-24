# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 02:42:58 2019

@author: 융
"""
dp=[]
n=int(input())
dp.extend([0,1,2])
for i in range(3,n+1):
    d=(dp[i-1]+dp[i-2])%10007
    dp.append(d)
print(dp[n])#멍청하게 dp[-1]하는바람에 n=0,1,2일때 안되게했음