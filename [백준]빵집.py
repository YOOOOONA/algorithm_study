import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
# R,C = map(int,input().split())
# mat = [list(input()) for _ in range(R)]

# #첫째열에서 건물x건너뛰고 맨 마지막 열로 도착하면서 겹치지않는 도로 개수의 최대값 리턴
move = [(-1,1),(0,1),(1,1)]#우상,우,우히#무조건 우사으로 먼저가야됨
r,c=map(int,input().split())
l=[list(input()) for _ in range(r)]
ans = 0
def dfs(i,j):
    global state, ans
    if i == -1 or i == r:
        return
    if l[i][j] == 'x':
        return
    l[i][j] = 'x'#이미 방문한 곳
    if j == c-1:
        state = True
        ans += 1
        return
    for a in range(3):
        dfs(i+move[a][0],j+move[a][1])
        if state:
            return

for i in range(r):
    state = False
    dfs(i,0)
print(ans)