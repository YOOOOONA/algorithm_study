import copy
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

N=int(input())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0

R = [(0,1),(1,1)]#가로로 있을때
C = [(1,0),(1,1)]#세로로 있을 때
D = [(0,1),(1,0),(1,1)]#대각으로 있을 때 진행방향
#진행경로가 (1,1)일 경우 두 칸 더 체크해야지
def solution(st,end,nb):
    #dfs
    global ans
    #현재 놓여진 방향 체크
    if st[0]==N-1 and st[1]==N-1:
        ans += 1
        return
        
    if st[0]-end[0]==0:
        dr = R
    elif st[1]-end[1]==0:
        dr = C
    else:
        dr = D
    
    for mv in dr:
        nxSt = tuple([st[0]+mv[0],st[1]+mv[1]])
        
        if nxSt[0]>=N or nxSt[1]>=N or board[nxSt[0]][nxSt[1]] == 1:
            continue
        if mv[0]==mv[1]==1:#대각으로 이동해야될 떄 체크
            if board[st[0]+1][st[1]] + board[st[0]][st[1]+1] != 0:
                continue
        #continue에 하나도 안걸렸으면 다음단계
        nb[nxSt[0]][nxSt[1]] = 2 
        solution(nxSt,st,nb)
        nb[nxSt[0]][nxSt[1]] = board[nxSt[0]][nxSt[1]]
board[0][1]=board[0][0] = 2
nb = copy.deepcopy(board)
solution((0,1),(0,0),nb)
print(ans)