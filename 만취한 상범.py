# -*- coding: utf-8 -*-
"""
Created on Thu May 23 22:59:22 2019

@author: 융
"""
'''입력
2//테스트 케이스 수
5//방개수=n이 5이상
100//100이하
출력
2
10

29056 KB,	72 ms 로 작성함
'''
t=int(input())
open=[0]*101
def test(t):
    
    for i in range(t):
        n = int(input())
        print(drunken(n))
        
def drunken(n):
    cnt=0
    for i in range(1,n+1):
        if(open[i]==0):
            for j in range(1,n+1):
                if(i>=j and i%j==0):
                    open[i]+=1
                elif(i<j):
                    break
        if(open[i]%2==1):
            cnt+=1
    return cnt
test(t)