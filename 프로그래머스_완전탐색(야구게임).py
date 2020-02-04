# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:52:56 2019

@author: 융
"""
"""
A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
[123,1,1]->123중 하나는 자리와 숫자 모두맞고 나머지 두개중하나가 순서만틀린거=>1,2,3:숫자가맞을수도,위치가 맞을수도
[3,5,6]->1개 숫자랑 위치맞고 나머지 두개는 포함안되는 숫자=>3,5,6숫자와 위치 동시에 맞을수도,쓰레기일수도
[3,2,7]->2개가 정답이고 하나는 쓰레기=>3,2,*&7아웃& 위에거떄문에 5,6쓰레기
[4,8,9]->1개만 숫자만맞고 2개는 쓰레기
"""

def solution(b_list):
    tot=list(filter(lambda x: "0" not in x and len(set(x))==3, list(map(str,[i for i in range(111,1000)]))))
    for b in b_list:
        i=0
        while len(tot) and i<len(tot):
            ss,st,bl=str(b[0]),0,0
            for j in range(len(ss)):
                if tot[i][j] in ss:
                    if tot[i][j]==ss[j]:
                        st+=1
                    else:
                        bl+=1
            if st!=b[1] or bl!=b[2]:
                tot.pop(i)
            else:
                i+=1
    return len(tot)


# 지금까지 생각을 이상하게 하고 있었다. 해당하는 숫자를 한자리씩 유추해야 한다고 생각해서 너무 어려웠는데 그게 아니라 모든 세자리 숫자를 bb에 제공된 모든 숫자와 비교해서 strike랑 ball개수가 bb에 제공된 숫자와 같을 시 후보로 넣어서 최종 개수를 출력하면 되는 문제였다.
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
