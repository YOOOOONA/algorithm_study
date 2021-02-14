from itertools import combinations
from collections import deque
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
N = int(input())#구역 개수
ppl = list(map(int,input().split()))#0구역부터 인구 정보 담김
graph_info = [[] for _ in range(N+1)]
for i in range(1,N+1):
    line = list(map(int,input().split()))
    graph_info[i] =[line[0],line[1:]]
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for p in graph_info[i][1]:
        board[i][p] = board[p][i] = 1
def linked(pts):#지역구 집합을 받을 떄 bfs로 하나로 연결됐는지 확인하기
    #bfs는 시작점을 잡는게 중요한데 걍 첫점으로
    st = pts[0]
    q = deque([[st,0],])
    visited = [0 for _ in range(len(pts))]
    while q:
        nx,idx = q.popleft()
        visited[idx] = 1#방문
        for i in range(len(pts)):
            if visited[i] != 1 and board[nx][pts[i]] == 1:
                q.append([pts[i],i])
    if sum(visited) != len(pts):
        return False
    else:
        return True
# def linked(pts):#구역 번호들 간에 연결이 되어있는지 확인
#     ans = False
#     if len(pts) == 1:
#         ans = True
#     elif len(pts) == 2:
#         if board[pts[0]][pts[1]] == 1:
#             ans = True
#     else:
#         ck = [0 for _ in range(N+1)]
#         for i in range(len(pts)):
#             for j in range(i,len(pts)):
#                 if sum(ck) == len(pts):
#                     ans = True
#                     return ans
#                 di,dj = pts[i],pts[j]
#                 if ck[di]*ck[dj] == 0 and board[di][dj] == 1 :                    
#                     ck[di] = ck[dj] = 1
#     return ans
def div(ppl):#ppl 정보를 
    As, Bs = [], []
    Appl, Bppl = [], []
    S = set(range(1,N+1))
    Tppl = sum(ppl)
    for i in range(1,N//2+1):
        for c in combinations(range(1,N),i):#1개부터 N-1개까지 comb구해서..
            As.append(list(S-set(c)));Appl.append(sum([ppl[j-1] for j in As[-1]]))
            Bs.append(list(c));Bppl.append(Tppl - Appl[-1])
    return As,Bs,Appl,Bppl

def yesDivide(ppl):
    ans = -1
    As,Bs,Appl,Bppl = div(ppl)
    #최소 한개이상구역가지고
    for i in range(len(As)):
        if linked(As[i]) and linked(Bs[i]):#A구역과 B구역 각각이 연결되어있을때
            diff = abs(Appl[i]-Bppl[i])
            ans = diff if ans == -1 else min(ans,diff)
    return ans
print(yesDivide(ppl))