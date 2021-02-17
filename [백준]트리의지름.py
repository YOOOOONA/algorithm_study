import sys
sys.stdin = open('.\\input.txt')

input = sys.stdin.readline

n=int(input())
tree_info = [[] for _ in range(n+1)]
ans = 0#최대 거리
farPt = 1
for _ in range(n-1):
    parent,child,length = map(int,input().split())
    tree_info[parent].append(tuple([child,length]))
    tree_info[child].append(tuple([parent,length]))#양방향이니까
    
def dfs(start,dist,visited):
    global ans,farPt
    for t in tree_info[start]:
        ch,w = t
        if visited[ch]==0:#방문안한점이면
            visited[ch] = 1#방문
            dfs(ch,dist+w,visited)
            visited[ch] = 0
        else:
            if ans<dist:
                ans = dist
                farPt = start
        
    return
visited = [0 for _ in range(n+1)]
start = 1
visited[start] = 1

dfs(start,0,visited)
print('첫',farPt,ans)
ans = 0
visited = [0 for _ in range(n+1)]
visited[farPt]=1
dfs(farPt,0,visited)     
print('두',farPt,ans)

print(ans)   