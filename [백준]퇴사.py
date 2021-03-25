import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

N = int(input())
due = [list(map(int,input().split())) for _ in range(N)]
maxPrf = -1
prf = 0
visited = [0 for _ in range(N)]
def dfs(start):
    global maxPrf,prf
    if start == N-1:
        visited[N-1] = 1
        if due[start][0] == 1:
            maxPrf = max(maxPrf,prf+due[start][1])
        else:
            maxPrf = max(maxPrf,prf)
        return
    #start를 하는 경우
    time,p = due[start]
    if start + time < N:
        prf += p
        visited[start] = 1
        dfs(start + time)
        prf -= p
        visited[start] = 0
    if start + 1 < N:#위에가 안되면 그냥 넘어가는 수밖에
        dfs(start + 1)#elif여도 그냥이어도 이 조건 성립
    #start를 일부러 안하는 경우도 위에 포함

    
dfs(0)
print(maxPrf,visited)