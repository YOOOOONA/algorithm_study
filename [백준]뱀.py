import sys
from heapq import heappush,heappop
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

N = int(input())#2<=<=100 보드 크기
K = int(input())#0<=<=100 사과 개수
# board = [[-1 if (i==0 or i==N or j==0 or j==N) else 0 for i in range(N+1)] for j in range(N+1)]
board = [[0 for _ in range(N)] for _ in range(N)]
def fin(head):
    if (head[0]<0 or head[0]>=N) or (head[1]<0 or head[1]>=N) or  board[head[0]][head[1]] == 1:#자기 몸
        return True
    else:
        return False#종료금지

def apple(head):
    if board[head[0]][head[1]] == 2:
        return True
    else:
        return False

for _ in range(K):#사과 위치
    i,j = map(int,input().split())
    board[i-1][j-1] = 2#사과있는곳은 2 #######퉤
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
    snake = []
    stI, stJ = 0,0#1,1에서 시작
    # path_pv = (0,1)#맨 처음엔 오른쪽으로 진행
    snake.append([stI,stJ])#시작 포인트
    board[stI][stJ] = 1
    while (True):
        for i in range(len(snakePath)+1):
            if i == 0:
                path = (0,1)
                X,C = snakePath[i]#다음방향대기
                
            elif i < len(snakePath):
                
                path = d[C][path]#path_pv
                X,C = snakePath[i]#시간,방향#X초 돌고 난 후에 방향 바꿔줘야지#다음방향 대기
                
            elif i==len(snakePath):
                path = d[C][path]
                X = 99999999999
            
                
            for _ in range(X-endTime):#이 시간이 중요포인트였음. 첨엔 그냥 X로만 했더니, 8초동안돌고 또 10초동안돌고 그랬음
                head = [snake[0][0]+path[0],snake[0][1]+path[1]]
                if fin(head):
                    return endTime+1
                endTime += 1
                if not apple(head):#head를 1로 만들기 전에 apple여부부터 확인해야됨
                    tail = snake.pop()#꼬리 자르기
                    board[tail[0]][tail[1]] = 0
                board[head[0]][head[1]] = 1
                head = [head,]
                head.extend(snake)#머리늘리기   #extend는 리턴이 none임
                snake = head
            
            
    return endTime#게임이 끝나는 시간
print(solve(board,snakePath))