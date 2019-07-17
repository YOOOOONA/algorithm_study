# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:02:30 2019

@author: 융
"""
'''
2 3//n m
1 2 4 ///배
8 16 32///열
3//k개 부분
1 1 2 3//1,1 부터 2,3까지의 합 구하기
1 2 1 2
1 3 2 3'''
n,m=map(int,input().split())

arr=[[int(x) for x in input().split()]for y in range(n)]

k=int(input())
x=[0]*2
y=[0]*2
for i in range(k):
    ret=0
    coord=[int(x) for x in input().split()]

    x[0]=coord[0]
    y[0]=coord[1]
    x[1]=coord[2]
    y[1]=coord[3]
    for j in range(x[0]-1,x[1]):
        for k in range(y[0]-1,y[1]):
            ret+=arr[j][k]
    print(ret)
