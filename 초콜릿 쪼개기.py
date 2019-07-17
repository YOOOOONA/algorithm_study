# -*- coding: utf-8 -*-
"""
Created on Thu May 23 23:54:18 2019

@author: 융
"""
'''
입력
2 2//n x m 행렬
출력
3//쪼개는 횟수
29056 KB	56 ms
'''
n , m = map(int, input().split())
def choco(n,m):
    cnt=n*m-1
    print(cnt)
choco(n,m)
    