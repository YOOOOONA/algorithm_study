# 체력은 진우가 이동할 수 있는 거리
# 민트초코우유를 마신다면 체력이 H 만큼 증가
# 최대한 우유 많이먹고 집에 돌어오는(중간에 체력0되지않을만큼)
import time
ST = time.time()
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
        if li[j] == 2:#우유위치
            MILK.append(tuple([i,j]))
ans = 0
milk = copy.deepcopy(MILK)
def dfs(milk,now,M):#먹은 우유개수, 먹은게 갱신된 지도, 현위치, 남은체력
    #체력이 닿는 곳 까지 다 돌았을 때 milk있는것들 다 담아야지
    global ans
    mk = copy.deepcopy(milk)
    for m in milk:
        move = abs(m[0]-now[0]) +abs(m[1]-now[1])
        if  move<= M:
            nM = M-move+H#현재체력-이동량+우유먹은체력
            if M>=0:#체력이 남아있으면
                tmp = now; now = m#현위치 바꾸고
                mk.remove(m)#먹었으니까 제거
                dfs(mk,now,nM)
                if now!=start:
                    if abs(start[0]-now[0]) +abs(start[1]-now[1]) <=nM:#현위치가 집이 아니고 집까지돌아갈수있으면
                        ans = max(ans,len(MILK)-len(mk))#원래우유개수-못먹은우유개수
                    
                #회복
                now = tmp#다시 for문 돌거니까
                mk.append(m)
dfs(milk,start,M)
print(ans)
END = time.time()
print(END-ST)