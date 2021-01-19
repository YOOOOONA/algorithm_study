import sys 
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
move = [(-1,-1),(-1,1),(1,-1),(1,1)]
# 최대로 비숍을 놓을 수 있는 개수
def color(i,j):
    #i,j위치를 기준으로 모든 대각선 다 0으로 
    colorList = []
    for k in range(4):
        dx,dy = i,j
        while 0<=dx<N and 0<=dy<N and board[dx][dy]!=0:#board내에서 놓을수있는지점까지
            if board[dx][dy] == -1: return False#이미 방문한 지점
            # board[dx][dy]=-1
            colorList.append([dx,dy])#-1을 대입할 후보
            dx,dy = dx+move[k][0],dy+move[k][1]
    return True

def dfs(black,white):
    stack = []#LIFO
    for n in black:
        i = n//N; j = n%N
        if board[i][j] == 1:
            color(i,j)
def solution(N):
    global board
    # #흑백 나눠서
    # 흑 백 흑
    # 백 흑 백
    # 흑 백 흑

    # 흑 백 0 1
    # 백 흑 2 3

    # 흑 백 흑 백 0 1 2 3 
    # 백 흑 백 흑 4 5 6 7
    # 흑 백 흑 백
    # 백 흑 백 흑
    black = []
    white = []
    for n in range(N*N):
        r = n//N
        c = n%N
        if r%2 == 0:#짝수 행
            if c%2 == 0: #짝수 열
                black.append(n)
            else:#홀수 열
                white.append(n)
        else:#홀수 행
            if c%2 == 0:#짝수 열
                white.append(n)
            else:
                black.append(n)
    dfs(black,white)
    # stack = []#LIFO
    # for n in black:
    #     i = n//N; j = n%N
    #     if board[i][j] == 1:
    #         color(i,j)
    return cnt

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]#비숍놓을수있으면 1,아니면 0
print(solution(N,board))


#이분매칭 알고리즘#A그룹과 B그룹의 짝을 찾아가는 알고리즘
def dfs(a):
    visited[a] = True
    for 











