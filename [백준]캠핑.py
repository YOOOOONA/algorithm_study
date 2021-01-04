# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 02:12:23 2020

@author: 융
"""

#캠핑장을 20일중 10일동안만 쓸수있고 28일치 휴가를 시작했는데 휴가 동안 캠핑장 며칠동안쓸수있나?
#이걸 일반화해서 , 연속하는 P일 중 L일동안만 사용할 수 있고 막 V일 짜리 휴가 시작했으면 최대 며칠 사용가능?
def solution(L,P,V):
    max_days = L * (V // P)
    res = V % P
    if res >= L:
        max_days += L
    elif res < L:
        max_days += res
    return max_days
if __name__ == '__main__':
    cnt = 1
    while(True):
        L, P, V = map(int,input("L, P, V:").split())
        if L==P==V==0: break
        else:
            ans = solution(L,P,V)
            print("Case %d: %d" %(cnt,ans))
            