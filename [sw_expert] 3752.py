# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:16:16 2020

@author: 융
"""

#가능한 시험점수
#input 
'''
2 T
3 N
2 3 5 시험 배점, 틀리면 0점 =>가질 수 있는 점수의 개수는?7(0+0+0,2,3,5(005,230),7, 8,10 )
10 N
1 1 1 1 1 1 1 1 1 1 =>11
'''
#집합으로 모든 조합 만든다음에 각 집합 합을 또 집합으로 만들면 중복 사라지지?
#조합 사용하면 런타임에러 피할 수 없음. 손코딩에서 조합코드 짜보라고 시킨대 ㄷㄷ
import itertools
#N=[2,3,5]
#N=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#ss=(1,2,3)
#print(sum(ss))
#print(sum(N))
T=int(input())
for _ in range(T):
    l=int(input())
    N=list(map(int,input().split()))
    a=[]
    s=set()
    for i in range(1,l+1):
        a.extend(list(itertools.combinations(N,i)))
        #print(a)
        #print(sum(a[0]))
    for i in range(len(a)):
        s.add(sum(a[i]))
        #s.add(sum(itertools.combinations(N,i)))
    s.add(0)
    print(len(s))
        