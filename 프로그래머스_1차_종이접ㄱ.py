# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:26:58 2019

@author: 융
"""
'''
                0                               n=1, bin[0] 길이 1
        0               1                       n=2,bin[0]+solution(1)[0]+bin[1] 길이 3
    0       1       0      1=>0010011           n=3,bin[0]+solution(2)[0]+bin[1]+solution(2)[1]+bin[1]+solution(2)[2]+bin[1]
0     1  0    1   0    1  0   1=> 001001100011011  사이공간을 벌려서 0101순서로 넣기
'''
bin=[0,1]
def solution(n):
    answer=[]
    if n==1:
        answer=[0]
    else:
        ran=len(solution(n-1))
        for i in range(ran+1):
            print("n",n)
            answer.append(bin[i%2])
            if(i!=ran):
                print(answer)
                answer.append(solution(n-1)[i])
            else:
                break
    return answer
print(solution(4))