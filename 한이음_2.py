# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:25:24 2019

@author: 융
"""

def knapsack(self, w,v,k):  # W: 배낭의 무게한도, wt: 각 보석의 무게, val: 각 보석의 가격, n: 보석의 수
    n=len(w)#######
    dp = [[0 for x in range(k+1)] for x in range(n+1)]  # DP를 위한 2차원 리스트 초기화
    for i in range(n+1):
        for j in range(k+1):  # 각 칸을 돌면서
            if i==0 or j==0:  # 0번째 행/열은 0으로 세팅
                dp[i][j] = 0
            elif w[i-1] <= j:  # 점화식을 그대로 프로그램으로
                dp[i][j] = max(v[i-1]+dp[i-1][j-w[i-1]], dp[i-1][j])  # max 함수 사용하여 큰 것 선택
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][k]
print(knapsack(50,[10,20,30],[60,100,120]))