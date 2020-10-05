# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:55:20 2020

@author: 융
"""

#분류 문제 solved.ac 브론즈1(너무 쉽)
def solution(N,fileList):
    #최대 50개의 최대길이 50의 파일이름 리스트를 받아서 패턴 파악
    #?는 최소로 사용
    ans = ''
    for idx,w in enumerate(fileList[0]):
        #0번째 파일이름을 기준으로 다 비교
        alph = w
        for ith in range(1,N):
            if fileList[ith][idx] == w:
                continue
            else:
                alph = '?'
                break
        ans += alph
    return ans
        
if __name__ == '__main__':
    N = int(input())
    fileList = [input() for _ in range(N)]
    print(solution(N,fileList))
