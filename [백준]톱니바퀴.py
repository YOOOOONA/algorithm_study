# 같은극일때 가만히
# 다른극일때 반대로 회전
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
from collections import deque
wheel = [deque(map(int,list(input()))) for _ in range(4)]
#회전횟수
K = int(input())
#회전방향.: 바퀴번호,방향(1:시계,-1:반시계)
rotation = [list(map(int,input().split())) for _ in range(K)]
deque.rotate()
#idx=2,6이 고려돼야됨
for i in range(K):
    whNum, dr = rotation[i]
    wheel[whNum].rotate(dr)

    if dr == 1:
        if 
        for j in range(4):
            if whNum != j:
                wheel[whNum].rotate(dr)
    elif dr == -1:
        for j in range(4):
            if whNum != j:

answer = 0
for i in range(4):
    if wheel[i][0] == 1:
        answer += 2**i
print(answer)
