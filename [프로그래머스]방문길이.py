# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:00:10 2020

@author: 융
"""

def solution(dirs):#dirs=경로 문자열
    answer = 0
    #전체 판 크기 11x11인데 한가운데(5,5)서 시작
    N = 11
    #UDRL=상하우좌
    dirD = {'U':(-1,0), 'D':(+1,0), 'R':(0,+1), 'L':(0,-1)}
    now = (5,5)
    visited = dict()
    visited[now] = []
    for d in dirs:
        move = dirD[d]
        nxt = tuple([now[0] + move[0], now[1] + move[1]])
        #여기서 길 중복 체크해야됨
        
        if 0<=nxt[0]<N and 0<=nxt[1]<N:
            if nxt not in visited[now]: 
                answer += 1
                visited[now].append(tuple(nxt))
                print(visited)
                if nxt not in visited.keys():
                    visited[nxt] = [tuple(now),]
                else:
                    visited[nxt].append(tuple(now))
            now = nxt
        else:#맵 밖으로 나가면 위치 갱신 안함
            continue
            
    return answer#지나간길이 중복제외하고 구하기 
print(solution("LULLLLLLU"))#7
'''
t=[(1,2),]
t.append( (2,3))
print(t)
'''