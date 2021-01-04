# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:47:49 2020

@author: 융
"""
import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    n = int(input())#문자열 길이
    
    wordList = [input() for _ in range(3)]#문자열 개수는 3개
    answer = 0
    for i in range(n):
        cnt = 0
        a = wordList[0][i]
        b = wordList[1][i]
        c = wordList[2][i]
        if a == b == c: 
            continue
        else:
            if a != b:cnt += 1
            if a != c:cnt += 1
            if b != c:cnt += 1
            #print(cnt)
            answer += cnt -1
    print('#{} {}'.format(tc,answer))