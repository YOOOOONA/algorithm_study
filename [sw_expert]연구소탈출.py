# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:55:28 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline


dr = [(-1,0),(+1,0),(0,-1),(0,+1)]

def move(direction):
    #방향을 입력받아서 이동할 수 있는지 확인하기
    #카운트세기
    #더 이동할 수 있는 0이 없는데
        #사방이 1이면 print("CANNOT ESCAPE")
        #그거 아니면 print("ZOMBIE")
        
def solution(N,M,mat):
    global mat
    
    ans = 0
    print(mat)
    #2는 1칸씩 확장
    matCopy = mat.copy()
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 2:
                for d in dr:#4방향 2 퍼뜨리기
                    matCopy[i+d[0]][j+d[1]] = 2 if mat[i+d[0]][j+d[1]] != 1 else None
            else:
                move
                    
    #3은 재귀로 모든 방향 가보기
    
    return ans
if __name__ == '__main__':
    T = int(input())
    for i in range(1,T+1):
        N, M = map(int,input().split())
        mat = [list(map(int,input().split())) for _ in range(N)]#0=No virus, 1=wall, 2=Yes virus, 3=my location
        print("#%d %d" %(i,solution(N,M,mat)))
        #break