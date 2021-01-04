# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 23:33:23 2021

@author: 융
"""

N,M = list(map(int,input().split()))#세로,가로
mat = [list(input().rstrip()) for _ in range(N)]#문자열은 rstrip()으로 쪼개줘야한다.
for i in range(N):
    for j in range(M):
        if mat[i][j] in ['R','B','O']:
            if mat[i][j] == 'R':
                r = [i,j]
            elif mat[i][j] == 'B':
                b = [i,j]
            elif mat[i][j] == 'O':
                o = [i,j]
#:장애물, .:이동가능, R,B,O:구멍
#visited = [[False for _ in range(M)] for _ in range(N)]
#이 4차원 visited행렬이 아주 key point였
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
queue = []#bfs는 큐 활용
#이동하기 전에 무조건 사방에 구멍있는지 ->벽있는지->이동

#가장 먼저 도달하는 순간을 특별히 생각할필요없이 그냥 순차적으로 돌다가 제일먼저 끝나는 순간이 제일 가까운순간임
visited[r[0]][r[1]][b[0]][b[1]] = True
queue.append((r,b,1))#왜 1이지?시작인데?
d = [(-1,0),(1,0),(0,-1),(0,1)]
def move(pt,dr):
    newI = pt[0]
    newJ = pt[1]
    cnt = 0
    while (mat[pt[0]][pt[1]] != 'O' and mat[newI][newJ] != '#'):
        pt = [newI,newJ]
        newI += d[dr][0]
        newJ += d[dr][1]
        cnt += 1#이동거리
        
    return pt,cnt#'O'나 '#'에 이미 도달한 포인트 리턴

def solve():
    while(queue):
        r,b,depth = queue.pop(0)
        if depth > 10: #1부터 시작했으니 10초과일때 out
            break #종료조건 2
        for i in range(4):
            new_r,rcnt = move(r,i)
            new_b,bcnt = move(b,i)
            if mat[new_b[0]][new_b[1]] != 'O':
                if mat[new_r[0]][new_r[1]] == 'O':
                   print(depth) #성공
                   return 
                #성공아닐떄
                if new_r == new_b:
                    if rcnt < bcnt:
                        new_b[0]-=d[i][0]
                        new_b[1]-=d[i][1]
                    else:
                        new_r[0]-=d[i][0]
                        new_r[1]-=d[i][1]
                if not visited[new_r[0]][new_r[1]][new_b[0]][new_b[1]]:
                    visited[new_r[0]][new_r[1]][new_b[0]][new_b[1]] = True
                    queue.append((new_r,new_b,depth+1))
    print(-1)#b가 'O'인 경우는 여기로 들어옴
solve()
#재귀돌아야겠다고 생각드는건 무조건 한단계 끝났을떄 q에 넣고 그다음 q를 받아서 하
        
        
        