import sys
sys.stdin=open('.\\input.txt')
input = sys.stdin.readline
from heapq import heappush, heappop
N = int(input())
space = [list(map(int,input().split())) for _ in range(N)]
# 0, 1~6, 9(아기상어위치)
# 처음 아기상어 크기 2
# 더이상 못먹으면 멈춤
fishList = []
mat = []
for i in range(N):
    row = list(map(int,input().split()))
    mat.append(row)
    for j in range(N):
        if row[j] == 9:
            shark = [2,[i,j]]
        elif 1 <= row[j] <= 6:
            heappush(fishList, [row[j] , (i,j)])#물고기 크기, 위치
dr = [(-1,0),(1,0),(0,-1),(0,1)]
def solution(fishList,shark):
    time = 0
    size,pos = shark

    if len(fishList)==0 or fishList[0][0] < size:
        print(time)
        return

    i, j = pos
    for k in range(4):
        ni,nj = i+dr[k][0],j+dr[k][1]
        if 0<=ni<N and 0<=nj<N:
            if space[ni][nj] < size:#물고기가 상어크기보다 작을때
  
            elif  space[ni][nj] == size:#같을떄
            else:#물고기가 더 클떄


# solution([1,2,4,6,8],3)
# def solution(li,target):
    
#     for i in range(len(li)):
#         if (target-li[i]) in li[i+1:]:
#             return True