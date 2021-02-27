import sys
import math
############이분탐색이 무조건 깡패
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) 

while start <= end: 
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    res=[i-mid if i>=mid else 0 for i in tree]
    log = sum(res)
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)