import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
#세로개수,가로개수,최대가로수
N,M,H = map(int,input().split())
# info = [list(map(int,input().split())) for _ in range(M)]
info = [[0 for _ in range(N+1)] for _ in range(H+1)]
for _ in range(M):
    a,b = map(int,input().split())
    info[a][b] = 1#좌
    info[a][b+1] = 2#우
cand = []
for i in range(1,H+1):
    for j in range(1,N):
        if sum(info[i][j:j+2]) == 0:
            cand.append([i,j])
answer = 4

def checkPath(info):
    #각자 어디로 도착하는지 체크
    check = [False for _ in range(1+N)]
    for i in range(1,N+1):
        cur = i
        for j in range(1,H+1):
            if info[j][cur] in [1,3]:
                cur += 1
            elif info[j][cur] in [2,4]:
                cur -= 1
        if i == cur:
            check[i] = True
    if sum(check) == N:
        return True#모두가 자기자신으로 간다
    else: 
        return False 
def solution(info):
    global answer
    if M == 0:
        answer = 0
        return
    solve(info,0,0)

def solve(info,i,cnt):
    global answer
    if cnt >= min(answer,3) or i>=len(cand): 
        return
    ni,nj = cand[i]
    solve(info,i+1,cnt)
    if sum(info[ni][nj:nj+2])==0:
        info[ni][nj]= 3
        info[ni][nj+1]=4
        if checkPath(info):
            answer = min(cnt+1,answer)
            
            info[ni][nj]= 0
            info[ni][nj+1]=0
            return

        solve(info,i+1,cnt+1)
        info[ni][nj]= 0
        info[ni][nj+1]=0
solution(info)
print(answer if answer<4 else -1)