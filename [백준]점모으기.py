import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())
x,y = [],[]
for _ in range(M):
    i,j = map(int,input().split())
    x.append(i)
    y.append(j)
midX = sorted(x)[M//2]#x,y의 중점이 곧 원하는 지점임.
midY = sorted(y)[M//2]
minDist = 0
for i in range(M):
    minDist += abs(x[i]-midX)+abs(y[i]-midY)
print(minDist)


# import sys
# sys.stdin = open('.\\input.txt')
# input = sys.stdin.readline

# N,M = map(int,input().split())
# spot = [list(map(int,input().split())) for _ in range(M)]#점 위치 1행1열부터 시작
# for i in range(M):
#     spot[i][0],spot[i][0] = spot[i][0] - 1 , spot[i][0] - 1
# def solve(N,M,spot):
#     minDist = 999999999
#     #모든점에 대해 다 거리 구하기    =>이러면 최악의 경우 O(N^3)나옴.
#     for i in range(N):
#         for j in range(N):
#             d = 0
#             for k in range(M):
#                 d += abs(spot[k][0]-i)+abs(spot[k][1]-j)
#             minDist = min(minDist,d)
#     return minDist#한점으로 모일 때 모든 점의 이동거리합의 최소값
# print(solve(N,M,spot))


