# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:15:40 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline
import copy
def recur(sp,way,now,rot):
    global largest
    #print('before',sp,now,way,rot)
    if rot == 3 and sp == now and len(way)>4:
        largest = max(largest,len(way)-2)#가장 많이 먹은 때의 경로길이 출력
        #print('아님 여기?',way)
        return
    if 0<=now[0]+dy[rot]<N and 0<=now[1]+dx[rot]<N:
        now[0] += dy[rot]; now[1] += dx[rot]
        
        #print(sp,'after',now,rot)
        
        if sp != now and len(set(way)) != len(way):
            #print('이건가',way)
            return
        
        
        
        #print('이건?')
        way.append(mat[now[0]][now[1]])
        #print(way,rot)
        if rot == 0:
            recur(sp,way,now,0)
            recur(sp,way,now,1) 
            recur(sp,way,now,2)
            recur(sp,way,now,3)
        elif rot == 1:
            recur(sp,way,now,1)
            recur(sp,way,now,2)
            recur(sp,way,now,3)
        elif rot == 2:
            recur(sp,way,now,2)
            recur(sp,way,now,3)
        elif rot == 3:
            recur(sp,way,now,3)
    else:
        #print('나옴')
        return

def solution():
    global largest
    
    for i in range(N):
        for j in range(N):
            sp = [i,j]
            #print(sp)
            way = [mat[i][j],]
            now = [i,j]
            rot = 0
            #print(way)
            recur(sp,way,now,rot)
            

if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        #4<=N<=20
        N = int(input())
        #디저트 종류 1이상 100이하. 같은 숫자 칸 못 지나감.한번씩만 갈수있음.출발한 카페로 돌아와야됨.대각선으로만 갈 수 있음.
        mat = [list(map(int, input().split())) for _ in range(N)]
        dx = [-1,1,1,-1]
        dy = [1,1,-1,-1]
        
        largest = -1#디저트를 못먹으면 -1임
        solution()
        print("#{} {}".format(tc+1, largest))
        #break