<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 03:03:05 2020

@author: 융
"""
def solution(board,pos,fut):
    '''
    나이트가 갈 수 있는 경로
    i-1,j-2
    i-2,j-1
    i-2,j+1
    i-1,j+2
    i+1,j-2
    i+2,j-1
    i+1,j+2
    i+2,j+1
    '''
    dy = {-1,-2,+1,+2}
    dx = {3 - abs(dy), abs(dy) - 3}
    for i in range(4):
        yp = pos[0] + dy[i]
        if yp > 0:
            if 0 <= pos[1] + dx[0] < I:
                xp = pos[1] + dx[0]
                flag = True
            elif 0 <= pos[1] + dx[1] < I:
                xp = pos[1] + dx[1]
                solution(board, [yp ,xp], fut)
                flag = True
            if flag == True and board[yp,xp] == 0:
                board[yp,xp] = solution(board, [yp ,xp], fut)
    return min_path
if __name__ == '__main__':
    T = int(input('T:'))#테스트케이스 개수
    for _ in range(T):
        I = int(input())#체스판 크기 IxI
        pos = list(map(int,input().split()))#현재 나이트의 위치 
        fut = list(map(int,input().split()))#나이트가 옮겨갈 위치
        board = [[0 * I] * I]
        ans = solution(board,pos,fut)#최소 이동 횟수 출력
        print('ans:',ans)
=======
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 03:03:05 2020

@author: 융
"""
def solution(board,pos,fut):
    '''
    나이트가 갈 수 있는 경로
    i-1,j-2
    i-2,j-1
    i-2,j+1
    i-1,j+2
    i+1,j-2
    i+2,j-1
    i+1,j+2
    i+2,j+1
    '''
    dy = {-1,-2,+1,+2}
    dx = {3 - abs(dy), abs(dy) - 3}
    for i in range(4):
        yp = pos[0] + dy[i]
        if yp > 0:
            if 0 <= pos[1] + dx[0] < I:
                xp = pos[1] + dx[0]
                flag = True
            elif 0 <= pos[1] + dx[1] < I:
                xp = pos[1] + dx[1]
                solution(board, [yp ,xp], fut)
                flag = True
            if flag == True and board[yp,xp] == 0:
                board[yp,xp] = solution(board, [yp ,xp], fut)
    return min_path
if __name__ == '__main__':
    T = int(input('T:'))#테스트케이스 개수
    for _ in range(T):
        I = int(input())#체스판 크기 IxI
        pos = list(map(int,input().split()))#현재 나이트의 위치 
        fut = list(map(int,input().split()))#나이트가 옮겨갈 위치
        board = [[0 * I] * I]
        ans = solution(board,pos,fut)#최소 이동 횟수 출력
        print('ans:',ans)
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
        