from collections import deque
def bfs(start,visited,computers):
    visited[start] = 1
    q=deque([start,])
    while q:
        pt = q.popleft()
        for i in range(len(computers[pt])):
            if computers[pt][i]==1 and visited[i]==0:
                visited[i] = 1
                q.append(i)
    return visited
            
def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for i in range(n):
        if visited[i] == 0:
            visited = bfs(i,visited,computers)
            answer += 1
    return answer#네트워크의 개수