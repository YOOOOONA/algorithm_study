# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:45:51 2019

@author: 융
"""
#10C3=10*9*8//1*2*3
n,k=map(int,input().split())
nom=1
denom=1
for i in range(1,k+1):
    nom*=(n-i+1)
    denom*=i
print(nom//denom%10007)