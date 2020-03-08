# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 00:35:38 2020

@author: 융
"""
#그리디 알고리즘
N=int(input())#회의 수
t_info=[list(map(int,input().split())) for _ in range(N)]#회의 시작시간,끝시간 리스트
#최대 사용 가능한 회의 수 를 출력
meeting = sorted(t_info,key=lambda x: (x[1],x[0]))

end=cnt=0
for m in meeting:
    if end<=m[0]:
        cnt+=1
        end=m[1]
print(cnt)