# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:31:09 2020

@author: 융
"""
############문제를 똑바로 안읽었다.."여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다"
'''내가 짠 코드 타임에러
def solution(n, lost, reserve):
    answer = 0
    for i in lost:
        print(i)
        if i-1 in reserve:
            reserve.remove(i-1)
        if i in reserve:
            reserve.remove(i-1)
        elif i+1 in reserve:
            reserve.remove(i+1)
        else: answer+=1
        print(lost,reserve)
    answer=n-answer
    return answer
'''
def solution(n,lost,reserve):
    set_reserve=set(reserve)-set(lost)
    set_lost=set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
print(solution(3,[1,2],[2,3]))#이게 2 나오는 코드가 정답 코드랜다..이상..이 아니고ㅠ "여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다."...
#############오늘의 교훈: 문제를 잘 읽자"