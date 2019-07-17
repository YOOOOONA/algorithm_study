# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:34:51 2019

@author: 융
"""
'''
1+1=2   1+2=3  1+3=4 / 1+4=5  2+5=7  2+7=9   3+9=12   4+12=16
1, 1, 2, 2, 3, 4, 5, 7, 9, 12 i = i-1 + i-5
'''
arr=[1,1,2,2,3]+[0]*100
n=int(input())
def pado_seq(n):
    for i in range(n):
        if arr[i]==0:
            arr[i]=(arr[i-1]+arr[i-5])
    return arr[n-1]
print(pado_seq(n))
            

