#스티커 점수 합 최대가 되게 스티커 떼기
# 뗄수있는 스티커 점수의 최댓값
# 한번떼면 상하좌우 다 못씀
import sys
import copy
sys.stdin = open('.\\input.txt')#output:260,290
input = sys.stdin.readline
from collections import deque
st=[]
n=0
def dfs(res,i,j,visit): 
    global ansLi
    #n==1일때 해야됨
    if res==i==j==0:
        dfs(res,1,0,visit)
    if j ==0:
        visit = [[0 for _ in range(n)] for _ in range(2)]
        visit[i][j]=1
        res+=st[i][j]
        i=(i+1)%2
        j+=1
    if j == n-1:
        visit_temp = copy.deepcopy(visit)
        visit_temp[i][j] = 1
        # print(res+st[i][j])
        ansLi.append(res+st[i][j])
        return
    elif j > n-1:
        # print(res)
        ansLi.append(res)
        return
    else:
        visit_temp = copy.deepcopy(visit)
        visit_temp[i][j] = visit_temp[(i+1)%2][j+1] = 1
        dfs(res + st[i][j] + st[(i+1)%2][j+1] , i,j+2,visit_temp)
        visit_temp = copy.deepcopy(visit)            
        visit_temp[i][j+1] = 1
        dfs(res + st[i][j+1] , (i+1)%2,j+2,visit_temp)
        
T = int(input())
for _ in range(T):
    n = int(input())
    ansLi = []
    st = [list(map(int,input().split())) for _ in range(2)]
    visit = [[0 for _ in range(n)] for _ in range(2)]
    res=0
    dfs(res,0,0,visit)
    print(max(ansLi))