# N×N의 격자판
# 행과 열의 번호는 1부터 시작한다. 각각의 칸은 빈 칸이거나 벽
# 파이프를 밀 수 있는 방향은 총 3가지,밀면서 회전  45도만 회전
import copy
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

N=int(input())
board = [list(map(int,input().split())) for _ in range(N)]
ans = 0
rot = [(0,1),(1,1),(1,0)]#우,우하,하
#start point와 endpoint가 있을때 endpoint는 startpoint를 가져가고 startpoint를 dr이용해서 갱신하는데 
#갱신될 st가 0이어야 가능
def checkNbr(nxSt,st):
    if board[st[0]][st[1]+1] == 0 and board[st[0]+1][st[1]] == 0:
        return True
    else:
        return False

def solution(nb,st,end):
    #dfs
    global ans
    
    if st==(N-1,N-1):
        ans += 1
        print(ans)
        return
    for i in range(3):
        nxSt = tuple([st[0]+rot[i][0],st[1]+rot[i][1]])
        if nxSt[0] >= N  or nxSt[1] >= N:
            continue
        if board[nxSt[0]][nxSt[1]] == 1:
            continue
    #갱신될 st와 갱신 전 st가 대각선이면 주변 세칸이 0이어야됨.
        #두 점이 대각선 관계일 떄 x,y둘다 좌표차이가 있음.
        if (nxSt[0]-st[0])*(nxSt[1]-st[1]) != 0:
            if not checkNbr(nxSt,st):
                continue
        nb[nxSt[0]][nxSt[1]] = 2 
        solution(nb,nxSt,st)
        nb[nxSt[0]][nxSt[1]] = board[nxSt[0]][nxSt[1]]

st = (0,1)
end = (0,0)
board[st[0]][st[1]] = board[end[0]][end[1]] = 2 
nb = copy.deepcopy(board)
solution(nb,st,end)
print(ans)