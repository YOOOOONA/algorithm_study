# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:08:09 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline
import copy
def recur():
    return way

def solution(N,rot,sp,way,now):
    global largest
    
    if rot == 3 and sp == now and len(way)>4:
        largest = max(largest,len(way)-1)#가장 많이 먹은 때의 경로길이 출력
        print('아님 여기?')
        return
    
    for i in range(N):
        for j in range(N):
            sp = [i,j]
            print(sp)
            way.append(mat[i][j])
        
            now[0] = i + dx[rot]
            now[1] = j + dy[rot]
            while True:
                now[0] += dx[rot];now[1] += dy[rot]
                if 0<=now[0]<N and 0<=now[1]<N:
                    if rot == 0:
                        dessert(N,0,sp,way,now)
                        dessert(N,1,sp,way,now)
                        dessert(N,2,sp,way,now)
                        dessert(N,3,sp,way,now)
                    elif rot == 1:
                        dessert(N,1,sp,way,now)
                        dessert(N,2,sp,way,now)
                        dessert(N,3,sp,way,now)
                    elif rot == 2:
                        dessert(N,2,sp,way,now)
                        dessert(N,3,sp,way,now)
                
                    elif rot == 3:
                        dessert(N,3,sp,way,now)
                else:return
            if len(set(way)) != len(way):
                print('여기 리턴?')
                return#way에 같은 값이 두개 이상 들어가면 way구할 필요없음
            #i,j위치에서 끝나면 way리셋
            way = []
        
if __name__ == '__main__':
    T = int(input())
    for tc in range(T):
        #4<=N<=20
        N = int(input())
        #디저트 종류 1이상 100이하. 같은 숫자 칸 못 지나감.한번씩만 갈수있음.출발한 카페로 돌아와야됨.대각선으로만 갈 수 있음.
        mat = [list(map(int, input().split())) for _ in range(N)]
        dx = [1,2,0,-1]
        dy = [-1,0,1,-1]
        largest = -1#디저트를 못먹으면 -1임
        rot = 0
        way = []
        sp = []
        now = []
        solution(N, rot, sp, way,now)
        print("#{} {}".format(tc+1, largest))