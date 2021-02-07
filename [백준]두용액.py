# 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고
# 오름차순으로 출력
# input
# 5
# output
# -2 4 -99 -1 98
import sys
input = sys.stdin.readline

N= int(input())
liq = sorted(list(map(int,input().split())))

start, end = 0,N-1
cstart,cend = start, end
czero=liq[0]+liq[-1]
while(start<end):
    tmp = liq[start]+liq[end]#cstart가 아니라 start를 넣고 정답으로 둘지말지 결정하는거지..
    if abs(tmp) < abs(czero):
        cstart = start
        cend = end
        czero = tmp
    if tmp < 0:
        start += 1
    else:
        end -= 1
print(liq[cstart],liq[cend])
# -99 -2 -1 4 98

# -9 -7 2 3 4
