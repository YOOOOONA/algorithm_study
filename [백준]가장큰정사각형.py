import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

n,m = map(int,input().split())
# 1로 된 가장 큰 정사각형의 크기
board = [list(map(int,list(input().strip()))) for _ in range(n)]#nxm배열
def solution(board):
    maxRgn = 0
    for i in range(n):
        for j in range(m):
            
            if board[i][j]!=0:
                k = 0
                flag = False
                while(True):
                    k+=1
                    if i+k>=n or j+k>=m or board[i+k][j+k]==0:
                        break
                    for ii in range(i,i+k):
                        if board[ii][j+k]==0:
                            flag = True
                            break
                    if flag: break
                    for jj in range(j,j+k):
                        if board[i+k][jj]== 0:
                            flag = True
                            break
                    if flag: break
                    
                maxRgn = max(maxRgn,k*k)
    return maxRgn
print(solution(board))