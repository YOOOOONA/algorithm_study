import sys
from collections import deque
sys.stdin = open('.\\input.txt')

input = sys.stdin.readline

n=int(input())
tree_info = [[] for _ in range(n+1)]
ans = 0#최대 거리
for _ in range(n-1):
    parent,child,length = map(int,input().split())
    tree_info[parent].append(tuple([child,length]))
    tree_info[child].append(tuple([parent,length]))#양방향이니까

def solution(start):
    q=deque([start,])
    visited = [-1 for _ in range(n+1)]
    visited[start] = 0#############################시작점으로 다시 돌아올때도 있는데 이 시작점은 이미 방문한 점이니까 0이 되어야하는데 다른값들도 0으로 디폴트셋팅해놓으면 구분이 안되니까 -1로 디폴트셋팅해놔야해!!!!!!!!!!!!!!!!!!!!!!!!!
    while(q):
        cur = q.popleft()
        for t in tree_info[cur]:
            nx,w = t
            if visited[nx]==-1:
                visited[nx] = visited[cur] + w#최단거리 찾을필요없이 그냥 한번 갱신이 끝임
                q.append(nx)
    ans = max(visited)
    farPt = visited.index(ans)
    return ans,farPt

print(solution(solution(1)[1])[0])
    
