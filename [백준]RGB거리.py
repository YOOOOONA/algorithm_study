# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:04:43 2020

@author: 융
"""
def f(res,now):
    global ans
    if now[0] == N-1: ans.append(res); return
    for i in range(2):
        nxt = [now[0] + move[i][0], (now[1] + move[i][1]) % 3]
        f(res + rgbList[nxt[0]][nxt[1]], nxt)
    

def solution(rgbList):
    res = 0
    for i in range(3):
        f(res + rgbList[0][i],[0,i])
    
    
move = [(1,1),(1,2)]#x축방향은 이거 더해주고 3으로 나눠줘야됨
ans = []
solution(rgbList)
print(min(ans))

###########################
#재귀가 능사가 아니다. dp로 min값 저장해서 넘기고 넘기고...해야