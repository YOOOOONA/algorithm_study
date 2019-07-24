# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 01:22:59 2019

@author: 융
"""
'''
2

5
50 10 100 20 40
30 50 70 10 60

7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.extend(b)
    print (a)
    s1=0
    s2=0
    for j in range(n):
        s1+=a[j*2]
        s2+=a[j*2+1]
    print(max(s1,s2))

#map을 list로 바꿔야 붙일수있음
a=map(int,input().split())
b=map(int,input().split())
a=a+b
print (a)
'''
def solve():
    d[1][0], d[1][1] = p[0][1], p[1][1]
    for i in range(2, n+1):
        d[i][0] = max(d[i-1][1], d[i-1][2]) + p[0][i]
        d[i][1] = max(d[i-1][0], d[i-1][2]) + p[1][i]
        d[i][2] = max(d[i-1][0], d[i-1][1], d[i-1][2])

for _ in range(int(input())):
    n = int(input())
    p = [[0]+list(map(int, input().split())) for _ in range(2)]#2차원 배열 받기
    d = [[0]*3 for _ in range(n+1)]
    solve()
    print(max(d[n]))

'''