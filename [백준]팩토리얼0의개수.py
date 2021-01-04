# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:03:46 2020

@author: 융
"""

N = int(input())#0<=N<=500
#0이 나오려면 2와 5 한쌍이 필요함
#N이하의 2의 배수 개수와 5의 배수 개수 min구하기
cnt = min(N//2,N//5)
print(cnt)#뒤에서부터 센 0의 개수