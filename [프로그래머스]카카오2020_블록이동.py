# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 01:47:24 2020

@author: 융
"""
from collections import deque
    
def can_move(cur1,cur2,new_board):
    Y, X = 0, 1
    cand = []
    #평행이동
    deltas = [(-1,0),(1,0),(0,1),(0,-1)]
    for dx,dy in deltas:
        nxt1 = (cur1[Y] + dy, cur1[X] + dx)
        nxt2 = (cur2[Y] + dy, cur2[X] + dx)
        if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
            cand.append((nxt1,nxt2))
    #회전
    if cur1[Y] == cur2[Y]:#가로방향일떄
        UP, DOWN = -1,1
        for d in [UP,DOWN]:
            if new_board[cur1[Y] + d][cur1[X]] == 0 and new_board[cur2[Y]+d][cur2[X]] == 0:
                cand.append((cur1,(cur1[Y]+d,))
        
def solution(board):
    #board 외벽 둘러싸기
    new_board = [[1 for _ in range(N+2)] for _ in range(N+2)]
    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[i][j]
    
    #현재 좌표 위치 큐 삽입, 확인용 set
    que = deque([((1,1),(1,2),0)])
    confirm = set([((1,1),(1,2))])
    
    while que:
        cur1, cur2, cnt = que.popleft()
        if cur1 == (N,N) or cur2 == (N,N):
            return cnt
        for nxt in can_move(cur1,cur2,new_board):
            if nxt not in confirm:
                que.append((*nxt,cnt+1))
                confirm.add(nxt)