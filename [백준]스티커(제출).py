#스티커 점수 합 최대가 되게 스티커 떼기
# 뗄수있는 스티커 점수의 최댓값
# 한번떼면 상하좌우 다 못씀
#recursion too mucg,, 점화식으로 풀어야됨. dfs가 아니라
import sys
import copy
sys.stdin = open('.\\input.txt')#output:260,290
input = sys.stdin.readline
from collections import deque
st=[]
n=0
def dfs(res,i,j): 
    global ansLi
    #n==1일때 해야됨
    if res==i==j==0:
        dfs(res,1,0)
    if j ==0:
        res+=st[i][j]
        i=(i+1)%2
        j+=1
    if j == n-1:
        ansLi.append(res+st[i][j])
        return
    elif j > n-1:
        ansLi.append(res)
        return
    else:
        dfs(res + st[i][j] + st[(i+1)%2][j+1] , i,j+2)
        dfs(res + st[i][j+1] , (i+1)%2,j+2)
        
T = int(input())
for _ in range(T):
    n = int(input())
    ansLi = []
    st = [list(map(int,input().split())) for _ in range(2)]
    res=0
    dfs(res,0,0)
    print(max(ansLi))