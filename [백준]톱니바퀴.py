# 같은극일때 가만히
# 다른극일때 반대로 회전
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
from collections import deque
wheel = [deque(map(int,list(input().strip()))) for _ in range(4)]
#회전횟수
K = int(input())
#회전방향.: 바퀴번호,방향(1:시계,-1:반시계)
rotation = [list(map(int,input().split())) for _ in range(K)]
#idx=2,6이 고려돼야됨

def do_rotate(left,right,rotdr):
    global wheel
    if len(left)>1:
        for i in range(1,len(left)):
            cur,nx = left[i-1:i+1]
            if wheel[cur][6] != wheel[nx][2] and rotdr[cur] != 0:
                dr = -rotdr[cur]
                rotdr[nx] = dr
                wheel[nx].rotate(dr)
    if len(right)>1:
        for i in range(1,len(right)):
            cur,nx = right[i-1:i+1]
            if wheel[cur][2] != wheel[nx][6] and rotdr[cur] != 0:
                dr = -rotdr[cur]
                rotdr[nx] = dr
                wheel[nx].rotate(dr)
            

for i in range(K):
    whNum, dr = rotation[i]
    whNum -= 1
    wheel[whNum].rotate(dr)
    #이동을 안하면 스킵해야되고 이동한 바로 옆애의 방향의 반대로 가야됨
    rotdr = [0 for _ in range(4)]
    rotdr[whNum] = dr#맨처음돌린애의 방향

    if whNum == 0:
        right = [0,1,2,3]
        left = [0]
        do_rotate(left,right,rotdr)


    if whNum == 1:
        right = [1,2,3]
        left = [1,0]
        do_rotate(left,right,rotdr)
    if whNum == 2:
        right = [2,3]
        left = [2,1,0]
        do_rotate(left,right,rotdr)
    if whNum == 3:
        right = [3]
        left = [3,2,1,0]
        do_rotate(left,right,rotdr)
    # elif whNum == 3:
    #     if wheel[whNum][6] != wheel[2][2]:
    #         wheel[2].rotate(-dr)
    #     if wheel[2][6] != wheel[1][2]:
    #         wheel[1].rotate(-dr)
    #     if wheel[1][6] != wheel[0][2]:
    #         wheel[0].rotate(-dr)
    
    
answer = 0
for i in range(4):
    if wheel[i][0] == 1:
        answer += 2**i
print(answer)
