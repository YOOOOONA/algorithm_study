import sys 
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
move = [(-1,-1),(-1,1),(1,-1),(1,1)]
# 최대로 비숍을 놓을 수 있는 개수
def color(i,j):
    #i,j위치를 기준으로 모든 대각선 다 0으로 
    for k in range(4):
        dx,dy = i,j
        while True:
            dx,dy = dx+move[k][0],dy+move[k][1]
            if 0<=dx<N and 0<=dy<N:
                board[dx][dy]=0
            else:
                break

def solution(N,board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                color(i,j)
    return cnt

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]#비숍놓을수있으면 1,아니면 0
print(solution(N,board))


#이분매칭 알고리즘#A그룹과 B그룹의 짝을 찾아가는 알고리즘
def dfs(a):
    visited[a] = True
    for 



