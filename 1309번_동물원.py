# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:58:10 2019

@author: 융
"""
'''
n*2배열의우리에 사자를 배치하는 경우의 수
n은 1에서 1000000이고 9901로 나눈 나머지 구해라
1 0
0 1
1 0
0 1
1 0
0 1
1 0

0 1
1 0
0 1
1 0
0 1
1 0
0 1
입력 4& 출력 41 잘 나오는데 ,,
''' #메모리 초과& 런타임 에러 128mb인데 235나옴
n=int(input())
#dp=[[0]*3 for i in range(n+1)]#2차원 배열 선언
dp[0][0]=1

def zoo(n):
    for i in range(n):
            
        dp[i+1][0] = dp[i][0] + dp[i][1] + dp[i][2] 
        
        dp[i+1][1] = dp[i][0] + dp[i][2]
        
        dp[i+1][2] = dp[i][0] + dp[i][1]

    return dp[n][0]+dp[n][1]+dp[n][2]
print(zoo(n)%9901)