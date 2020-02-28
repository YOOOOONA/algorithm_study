
from collections import deque #큐를 빨리 돌리기위함

#BFS함수 정의
def bfs1(i, j):
    queue = deque()
    queue.append([i, j])
    color = grid[i][j] #하나의 컬러만
    
    while queue:
        [i, j] = queue.popleft()
        visited[i][j] = True
        
        if i + 1 < N and [i+1, j] not in queue and visited[i+1][j] == False and grid[i+1][j] == color:
            queue.append([i+1, j])
        if i - 1 >= 0 and [i-1, j] not in queue and visited[i-1][j] == False and grid[i-1][j] == color:
            queue.append([i-1, j])
        if j + 1 < N and [i, j+1] not in queue and visited[i][j+1] == False and grid[i][j+1] == color:
            queue.append([i, j+1])
        if j - 1 >= 0 and [i, j-1] not in queue and visited[i][j-1] == False and grid[i][j-1] == color:
            queue.append([i, j-1])
            
    return #아무것도 리턴해주지 않아도됨(실행 자체로 의미)

def bfs2(i, j):
    queue = deque()
    queue.append([i, j])
    color = grid[i][j] #하나의 컬러만
    if color=='R' or color=='G':
        while queue:
            [i, j] = queue.popleft()
            visited[i][j] = True
            
            if i + 1 < N and [i+1, j] not in queue and visited[i+1][j] == False and (grid[i+1][j] == 'R' or grid[i+1][j] == 'G'):
                queue.append([i+1, j])
            if i - 1 >= 0 and [i-1, j] not in queue and visited[i-1][j] == False and grid[i-1][j] == color:
                queue.append([i-1, j])
            if j + 1 < N and [i, j+1] not in queue and visited[i][j+1] == False and grid[i][j+1] == color:
                queue.append([i, j+1])
            if j - 1 >= 0 and [i, j-1] not in queue and visited[i][j-1] == False and grid[i][j-1] == color:
                queue.append([i, j-1])
                
        return #아무것도 리턴해주지 않아도됨(실행 자체로 의미)
    else:
        while queue:
            [i, j] = queue.popleft()
            visited[i][j] = True
            
            if i + 1 < N and [i+1, j] not in queue and visited[i+1][j] == False and grid[i+1][j] == color:
                queue.append([i+1, j])
            if i - 1 >= 0 and [i-1, j] not in queue and visited[i-1][j] == False and grid[i-1][j] == color:
                queue.append([i-1, j])
            if j + 1 < N and [i, j+1] not in queue and visited[i][j+1] == False and grid[i][j+1] == color:
                queue.append([i, j+1])
            if j - 1 >= 0 and [i, j-1] not in queue and visited[i][j-1] == False and grid[i][j-1] == color:
                queue.append([i, j-1])
                
        return #아무것도 리턴해주지 않아도됨(실행 자체로 의미)
#인풋
N = int(input())
grid = [input() for _ in range(N)] #RGB 인풋

visited = [[False for _ in range(N)] for _ in range(N)] #방문 했는가
answer_1 = 0 #몇 구역
for i in range(N):
    for j in range(N):
        if not visited[i][j]: #방문 안했을 시
            bfs1(i, j) #방문
            answer_1 += 1 #그룹 + 1


visited = [[False for _ in range(N)] for _ in range(N)]
answer_2 = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs2(i, j)
            answer_2 += 1
            
print(answer_1, answer_2)