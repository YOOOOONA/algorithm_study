import sys
from heapq import heappush,heappop
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

N = int(input())#2<=<=100 보드 크기
K = int(input())#0<=<=100 사과 개수
board = [[-1 if (i==0 or i==N or j==0 or j==N) else 0 for i in range(N+1)] for j in range(N+1)]

for _ in range(K):#사과 위치
    i,j = map(int,input().split())
    board[i][j] = 2#사과있는곳은 2
L = int(input())
snakePath = []
for _ in range(L):#뱀의 이동경로 X:X초후에 C:C방향으로 이동(L:왼쪽, D:오른쪽)
    X, C = input().split()
    X = int(X)
    snakePath.append([X,C])
d = {'L':{(0 , 1):(-1, 0),
          (-1, 0):(0 ,-1),
          (0 ,-1):(1 , 0),
          (1 , 0):(0 , 1)},
     'D':{(-1, 0):(0 , 1),
          (0 ,-1):(-1, 0),
          (1 , 0):(0 ,-1),
          (0 , 1):(1 , 0)}}
def solve(board,snakePath):
    #뱀이 자기자신과 만나거나 벽에 부딪히면 끝남
    endTime = 0
    path = []
    snake = []
    stI, stJ = 1,1#1,1에서 시작
    path.append([0,1])#맨 처음엔 오른쪽으로 진행
    snake.append([stI,stJ])#시작 포인트
    #dr = ''#왼쪽갈지 오른쪽갈지
    while (True):
        X,C = snakePath.pop(0)#시간,방향

        for i in range(X):
            for j in range(len(snake)):
                path[j] 
        #사과를 만나는지 여부는 대가리만 확인하고 지나면서 뱀으로 덮고 뱀지나가면 0으로 만들면 사과사라짐

        #벽에 닿았는지 확인
        #자기자신에 닿았는지 확인


    return endTime#게임이 끝나는 시간
print(solve(board,snakePath))