from collections import deque
# 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이
n=int(input())
#루트=1
# tree = [list(map(int,input().split())) for _ in range(n)]#부모노드번호,자식노드,간선가중치
#생각없이 트리 받지 말고 부모와 자식간의 관계가 보이게 인접으로
tree_info = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent,child,length = map(int,input().split())
    tree_info[parent].append([child,length])

#bfs로 루트부터 나머지 노드번호 정렬하기(탐색순서정하는거)
def bfs(graph_list,start):
    q=deque([start,])
    visited = []
    while(q):
        node = q.pop(0)
        visited.append(node)
        for child in graph_list[node]:
            q.append(child[0])
    return visited

bfs_node = bfs(tree_info,1)
max_node = [0 for _ in range(n+1)]
diameter = [[0] for _ in range(n+1)]
max_diameter = [0 for _ in range(n+1)]

while bfs_node:
    tmp = bfs_node.pop()#뒤에부터 거꾸로
    for child in tree_info[tmp]:
        try:
            child_length = max_node[child[0]] + child[1]
        except:
            child_length = child[1]
        diameter[tmp].append(child_length)
        max_node[tmp] = max(diameter[tmp])
    max_diameter[tmp] += max(diameter[tmp])
    diameter[tmp].remove(max(diameter[tmp]))
    try:
        max_diameter[tmp] += max(diameter[tmp])
    except:
        
