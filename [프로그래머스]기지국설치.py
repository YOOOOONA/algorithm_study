# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:30:23 2020

@author: 융
"""

def solution(n, stations, w):
    answer = 0
    
    st = [0 for _ in range(n+1)];st[0]=1
    
    for a in stations: 
        l = max(1,a-w)
        r = min(n+1,a+w+1)
        for j in range(l,r):
            st[j] = 1
    cnt = []
    flag = 0
    
    for i in range(1,n+1):
        if st[i] == 0 and flag == 0:
            c = 1
            flag = 1
        elif st[i] == 0 and flag == 1:
            c += 1
            if i == n: cnt.append(c)
        elif st[i] == 1 and flag == 1: 
            cnt.append(c)
            flag = 0
        
    rng = 2*w+1
    for c in cnt:
        if c<= rng: answer += 1
        else: 
            if c % rng > 0 : answer += c // rng + 1
            else: answer += c // rng
    
    return answer#모든 아파트에 전파 전달 위해 증설해야될 기지국 최소 개수 리턴
print(solution(16,[9],2))
print(solution(11,[4,11],1))


#다른사람코

def solution(n, s, w):
    answer=0
    idx = 0
    locate = 1
    while locate <=n:
        if idx < len(s) and locate >= s[idx]-w:
            locate = s[idx]+w+1
            idx+=1
        else:
            locate += 2*w+1
            answer+=1
    return answer