# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:09:47 2020

@author: 융
"""
'''
import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def countBlock(W,H,mat):
    #블럭있는 칸 수 세서 리턴
    cnt = W * H
    for l in mat:
        cnt -= l.count(0)
    return cnt


def crushBlock(N,W,H,mat):
    global blockCnts
    #N개 구슬 떨군 뒤에 남을 최소의 벽돌 개수 리턴
    if N == 0:#구슬 다 떨궜으면
        blockCnts.append(countBlock(W,H,mat))
    
    for j in range(W):
        #i번째 블록 없앤 뒤의 mat상태 리턴해줘야돼
        ##################################
        #i콜롬,젤 상단 로우 찾아ㅓ 걔 값알아서 그 값만큼 상하좌우 지워야돼
        for i in range(H):
            r = mat[i][j]
            if r == 0: continue
            else:
                li = i-(r-1) if i-(r-1) > 0 else 0; ri = i+(r-1) if i+(r-1) < W-1 else W-1 
                mat[li:ri][j] = 0
                lj = j-(r-1) if j-(r-1) > 0 else 0; rj = j+(r-1) if j+(r-1) < H-1 else H-1
                mat[i][lj:rj] = 0
                print('i와 mat',i,'\n',mat,'\n')
                break
        ##################################
        crushBlock(N-1,W,H,mat)
    print(mat,'\n')


if __name__ == '__main__':
    print('a')
    T = int(input())
    print(T)
    for tc in range(T):
        #1<=N<=4, 2<=W<=12, 2<=H<=15
        N, W, H = map(int, input().split())
        print(N)
        mat = [list(map(int, input().split())) for _ in range(H)]
        blockCnts = []
        crushBlock(N,W,H,mat)
        print("#{} {}".format(tc+1, max(blockCnts)))
'''
a = [[0,0,0,1],[2,1,3,0]]
for i in a:
    print(i.count(0))
for i in range(2):
    a[i][2] =999
print(a)