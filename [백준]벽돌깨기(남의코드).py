# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 22:52:44 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline
import copy
def dfs(idx,mat):
    global blockCnts#새로운 값을 넣을 때만 글로벌 해주면 됨
    if idx == N:#구슬 N번 떨구면 재귀 끝
        cnt = 0
        for z in range(H):
            cnt += mat[z].count(0)
        resultCnt = W*H - cnt
        if resultCnt < blockCnts:
            blockCnts = resultCnt
        return
    
    for y in range(W):#구슬 쏘는 위치 (열)
        check = 0
        for x in range(H):
            if not mat[x][y]:#0이면
                continue
            else:#0이아니면
                init_mat = copy.deepcopy(mat)#.copy()
                q = [(x,y,mat[x][y])]
                while q:#가능한 벽돌 다 터뜨림
                    qq = q.pop(0)
                    if qq[2] == 1:#블록이 1이면
                        mat[qq[0]][qq[1]] = 0#자기자신만 0으로
                    else:
                        mat[qq[0]][qq[1]] = 0
                        for k in range(1,qq[2]):
                            for i in range(4):
                                _x = qq[0] + dx[i]*k
                                _y = qq[1] + dy[i]*k
                                if (0<= _x <H) and (0<= _y <W) and mat[_x][_y] != 0:
                                    if (_x,_y,mat[_x][_y]) not in q:
                                        q.append((_x,_y,mat[_x][_y]))
                mat2 = [[0 for _ in range(W)] for _ in range(H)]
                for j in range(W):#빈틈없이 벽돌 쌓기
                    tmp = []
                    for i in range(H):
                        if mat[i][j]:
                            tmp.append(mat[i][j])
                    for a in range(len(tmp)):
                        mat2[H-len(tmp)+a][j] = tmp[a]
                check = 1
            if check == 1:#y행x열에서 할 수 있는 짓 다 했으니 다음으로 넘어간다
                dfs(idx+1,mat2)
                mat = init_mat
                break#밑에칸으로 내려가서 진행할 필요없음 다음 열로 가야됨
    dfs(N,mat)#모든 행,열 다 돌았으면 끝인데 그냥 break하면 안되고 마지막까지 개수 구해야지
'''

import copy
def dfs(idx,mapp2):
    global block_cnt
    if idx == N: # 종료 기준 = 슛팅횟수만큼 탐색
        cnt = 0
        for z in range(H): # 0을 세서 전체 리스트 요소 개수에서 빼주면 남은 벽돌 개수가 나옴
            cnt += mapp2[z].count(0)
        result_cnt = W*H - cnt
        if result_cnt < block_cnt:
            block_cnt = result_cnt
        return
 
    for y in range(W): # 구슬 쏘는 위치(열)
        check = 0
        for x in range(H): # 가장 위에 있는 벽돌을 찾음 (행)
            if not mapp2[x][y]: # 맵이 0이면 블록이 없다는 뜻이기에 다음 행 탐색
                continue
            else: 
                init_mapp = copy.deepcopy(mapp2) # 초기맵 복사 // 맵을 터뜨릴꺼기에 백트래킹 때 맵 복구를 위해서
                q = [(x,y,mapp2[x][y])] 
                while q: # BFS // 가능한 벽돌 다 터뜨림
                    qq = q.pop(0)
                    if qq[2] == 1: #블록숫자가 1이면 자기만 터짐
                        mapp2[qq[0]][qq[1]] = 0
                    else:
                        mapp2[qq[0]][qq[1]] = 0 
                        for k in range(1,qq[2]): # 블록 숫자 - 1만큼 연쇄폭발
                            for i in range(4):
                                if 0 <= qq[0]+dx[i]*k < H and 0 <= qq[1]+dy[i]*k < W and mapp2[qq[0]+dx[i]*k][qq[1]+dy[i]*k] != 0:
                                    if (qq[0]+dx[i]*k,qq[1]+dy[i]*k,mapp2[qq[0]+dx[i]*k][qq[1]+dy[i]*k]) not in q: # 큐에 중복으로 들어가는 것 방지                  
                                        q.append((qq[0]+dx[i]*k,qq[1]+dy[i]*k,mapp2[qq[0]+dx[i]*k][qq[1]+dy[i]*k]))
            
                mapp3 = [[0 for _ in range(W)] for _ in range(H)]
                for j in range(W): # 벽돌 아래로 내리는 작업
                    temp = []
                    for i in range(H):
                        if mapp2[i][j]:
                            temp.append(mapp2[i][j])   
                    for a in range(len(temp)):
                        mapp3[H-len(temp)+a][j] = temp[a]
                check = 1 # 선택된 열에서 가장 높은 위치의 벽돌을 찾는 것이기에 행을 찾게 되면 그 다음 행을 탐색하면 안되기에 check를 통해 방지
            if check == 1: 
                dfs(idx+1,mapp3)
                mapp2 = init_mapp
                break
    dfs(N,mapp2) # 모든 행 열을 탐색해도 벽돌이 없다면 종료시킬 것임
'''
if __name__ == '__main__':
    T = int(input())
    print(T)
    for tc in range(T):
        #1<=N<=4, 2<=W<=12, 2<=H<=15
        N, W, H = map(int, input().split())
        print(N)
        mat = [list(map(int, input().split())) for _ in range(H)]
        blockCnts = 999999999
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        dfs(0,mat)
        print("#{} {}".format(tc+1, blockCnts))
        #break