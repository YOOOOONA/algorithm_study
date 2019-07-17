# -*- coding: utf-8 -*-
"""
Created on Sat May 11 20:27:38 2019

@author: 융
1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요
"""
a1=[1,2,3,4,5]
a2=[2,1,2,3,2,4,2,5]
a3=[3,3,1,1,2,2,4,4,5,5]
def solution(answers):
    answer = []
    cnt1=0
    cnt2=0
    cnt3=0
    for i in len(answers):
        if(answers[i]==a1[i%5]):
            cnt1+=1
        if(answers[i]==a2[i%8]):
            cnt2+=1
        if(answers[i]==a3[i%10]):
            cnt3+=1
    max_cnt=max(cnt1,cnt2,cnt3)
    if(cnt1>=max_cnt):
        answer.append(1)
    if(cnt2>=max_cnt):
        answer.append(2)
    if(cnt3>=max_cnt):
        answer.append(3)
    return answer

