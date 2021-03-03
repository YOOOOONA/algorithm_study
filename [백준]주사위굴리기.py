import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

N,M,x,y,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
move = list(map(int,input().split()))
dr = [(),(0,1),(0,-1),(-1,0),(1,0)]
def rotate(dr,dice):
    if dr == 1:
        #동
        tmp = dice[6]
        dice[6] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp
    elif dr == 2:
        #서
        tmp = dice[6]
        dice[6] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp
    elif dr == 3:
        #북
        tmp = dice[3]
        dice[3] = dice[2]
        dice[2] = dice[1]
        dice[1] = dice[4]
        dice[4] = tmp
    elif dr == 4:
        #남
        tmp = dice[3]
        dice[3] = dice[4]
        dice[4] = dice[1]
        dice[1] = dice[2]
        dice[2] = tmp
    return dice

def solution():
    dice = {1:0,2:0,3:0,4:0,5:0,6:0}#1바닥,3윗면,5,6왼오
    

    loc = [x,y]
    for i in move:
        loc[0] += dr[i][0] 
        loc[1] += dr[i][1]
        if 0<=loc[0]<N and 0<=loc[1]<M:
            dice = rotate(i,dice)

            if board[loc[0]][loc[1]] == 0:
                board[loc[0]][loc[1]] = dice[1]
            else:
                dice[1] = board[loc[0]][loc[1]]
                board[loc[0]][loc[1]] = 0
            print(dice[3])
        else:
            loc[0] -= dr[i][0] 
            loc[1] -= dr[i][1]
solution()