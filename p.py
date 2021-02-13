# 각 선거구가 이어져있는지 bfs로 확인
# 이어져있지않으면 bfs에서 0 반환하고 이어져있으면 인구수 반환
# 인구수 차 최소값을 계속 기록
from collections import deque
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

def bfs(start):
    q=deque()
    q.append(start)
    while q:
        nx = q.popleft()
        
def dfs(cnt,x,end):#조합만들기
    global min_ans
    if cnt == end:
        g1,g2 = deque(), deque()
        for i in range(n):
            if c[i]:
                g1.append(i)
            else:
                g2.append(i)
        ans1 = bfs(g1)
        if not ans1:
            return
        ans2 = bfs(g2)
        if not ans2:
            return
        min_ans = min(min_ans, abs(ans1-ans2))
        return
    for i in range(x,n):
        if c[i]:
            continue
        c[i] = 1
        dfs(cnt+1,i,end)
        c[i] = 0
n = int(input())
people = list(map(int, input().split()))

a = [[] for _ in range(n)]
for i in range(n):
    x = list(map(int, input().split()))
    a[i] = [k-1 for k in x[1:]]
min_ans = -1
for i in range(1,n//2+1):
    c = [0 for _ in range(n)]
    dfs(0,0,i)
print(min_ans)
