# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:42:07 2019

@author: 융
"""
'''
입력
3 4//미로크기 n x m
1 2 3 4
0 0 0 5
9 8 7 6
출력
31
'''
'''
a=[[1,2],[1,2],[1,2],[1,2],[1,2]]
a[2][0]=a[2][0]+max(a[-1][0],a[1][1],a[0][-1]) okok!
'''
n,m=map(int,input().split())

arr=[[int(x) for x in input().split()]for y in range(n)]
dp=[n][m]

for i in range(n):
    
    for j in range(m):
        dp[i][j] = arr[i][j] + max(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
print(arr)