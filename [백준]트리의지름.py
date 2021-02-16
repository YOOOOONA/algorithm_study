from collections import deque
# 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이=
#트리에서 임의의 점(루트로 설정) 에서 가장 먼 점(A)을 찾고, 그 점에서 다시 가장 먼 점(B)을 찾으면
#A에서 B까지의 거리가 지름이 됨
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

n=int(input())
#루트=1
# tree = [list(map(int,input().split())) for _ in range(n)]#부모노드번호,자식노드,간선가중치
#생각없이 트리 받지 말고 부모와 자식간의 관계가 보이게 인접으로
tree_info = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent,child,length = map(int,input().split())
    tree_info[parent].append(tuple([child,length]))
def bfs(start):#start에서 가장 먼 노드 찾아내기
    dist = 0
    farPt = None
    q = deque([(start,0),])#(노드,거리)
    while(q):
        cur_node,cur_w = q.popleft()
        if len(tree_info[cur_node]) == 0:#리프노드일때
            if dist < cur_w:#더 먼거리면
                farPt = cur_node
                dist = cur_w
        else:#리프노드 아닐때
            for ti in tree_info[cur_node]:
                nx_node, nx_w = ti#부모후보,cur과 ti사이 거리
                q.append(tuple([nx_node,cur_w + nx_w]))
    return farPt, dist#dist = start와 farPt 사이의 최단 거리 

# [
#     []
#     [(2,3),(3,4)]#1번노드에 연결된 자식노드와 웨이트
#     [(4,5),(5,4)]#2버노드에 연결된,,
# ]
def remakeTree():# = 자식이 부모로, 부모가 자식으로 들어가면되고 웨이트는 그대로
    reverse_tree_info = [[] for _ in range(n+1)]
    for i in range(1,n+1):
        t = tree_info[i]
        for j in t:
            reverse_tree_info[j[0]].append(tuple([i,j[1]]))#parent와 child를 바꾼
    # # print(reverse_tree_info)
    # new_tree_info = [[] for _ in range(n+1)]
    # new_tree_info[node].append()
    return reverse_tree_info


A,_ = bfs(1)
tree_info = remakeTree()
B,dist = bfs(A)# (루트(=1번노드)의 farPt )의 farPt
print(dist)#A에서 B까지의 최단거리 

# remakeTree(1)