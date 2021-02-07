# 체력은 진우가 이동할 수 있는 거리
# 민트초코우유를 마신다면 체력이 H 만큼 증가
# 최대한 우유 많이먹고 집에 돌어오는(중간에 체력0되지않을만큼)
def solution():

    return ans#최대우유개수
import sys
sys.stdin = open(".\\input.txt")
input = sys.stdin.readline
#마을크기,초기체력,증가체력
N,M,H = list(map(int,input().split()))
#1=집,2=우유
board = [list(map(int,input().split())) for _ in range(N)]
#output:2,8