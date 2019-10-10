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

#남의 코드 1
def solution(baseball):
    answer = 0
    for i in range(123,988):
        x=str(i)
        if x.count(x[0])>=2 or x.count(x[1])>=2 or x.count('0')>=1:
            continue
        c=0
        for j in baseball:
            st=0
            ba=0
            y=str(j[0])
            for k in range(0,3):
                if x[k]==y[k]:
                    st+=1
                elif y.count(x[k])==1:
                    ba+=1
            if st!=j[1] or ba!=j[2]:
                c=1
                break
        if c==0:
            answer+=1
    return answer

#남의 코드 2
def solution(bb):#bb는 2차원 배열
    rs=list(filter(lambda x: "0" not in x and len(set(x)) ==3, list(map(str,range(111,1000)))))#0안들어가고 길이 3인 x만 모아
    for b in bb:
        i=0
        while len(rs) and i<len(rs):
            ss, st, bl = str(b[0]),0,0
            for j in range(len(ss)):
                if rs[i][j] in ss:
                    if ss.index(rs[i][j])==j:
                        st +=1
                    else:
                        bl +=1
            if st !=b[1] or bl != b[2]:
                rs.pop(i)
            else:
                i +=1                
    return len(rs)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            )))