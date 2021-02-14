# 체력은 진우가 이동할 수 있는 거리
# 민트초코우유를 마신다면 체력이 H 만큼 증가
# 최대한 우유 많이먹고 집에 돌어오는(중간에 체력0되지않을만큼)
import copy
import sys
sys.stdin = open(".\\input.txt")
input = sys.stdin.readline
#마을크기,초기체력,증가체력
N,M,H = list(map(int,input().split()))
#1=집,2=우유
board = []
MILK = []
for i in range(N):
    li = list(map(int,input().split()))
    board.append(li)
    if 1 in li:#집의 위치
        start = tuple([i,li.index(1)])
    for j in range(N):
        if li[j] == 2:
            MILK.append([i,j])
ans = 0
nb = copy.deepcopy(board)
milk = copy.deepcopy(MILK)
def dfs(milk,nb,now,M):#먹은 우유개수, 먹은게 갱신된 지도, 현위치, 남은체력
    #체력이 닿는 곳 까지 다 돌았을 때 milk있는것들 다 담아야지
    global ans
    for m in milk:
        move = abs(m[0]-now[0]) +abs(m[1]-now[1])
        if  move<= M:
            M = M-move+H#현재체력-이동량+우유먹은체력
            if M>=0:#체력이 남아있으면
                now = m#현위치 바꾸고
                milk.remove(m)#먹었으니까 제거
                nb[m[0]][m[1]] = 3
                dfs(milk,nb,now,M)
                nb[m[0]][m[1]] = board[m[0]][m[1]]
        if now!=start and abs(start[0]-now[0]) +abs(start[1]-now[1]) <=M:#현위치가 집이 아니고 집까지돌아갈수있으면
            ans = max(ans,len(MILK)-len(milk))#원래우유개수-못먹은우유개수
            now = start#집으로 돌아옴
            

dfs(milk,nb,start,M)
print(ans)
#output:2,8

# 일단 갈 수 있는 모든 경우의수를 q에 넣고 해당 지점에서 집으로 돌아올수있으면 돌아오고
# 집으로 가는 여부와 상관없이 다른 지점으로 갈수 있으면 간다. 
