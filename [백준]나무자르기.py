import sys
import math
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
N,M = map(int,input().split())#나무 수, 나무길이(1이상)
tree = sorted(list(map(int,input().split())),reverse=True)#나무 높이들.총 합은 항상 M보다 크거나같고 각각은 0일 수 있음
# 필요한만큼만 가져가기 위해 나무를 최대한 길게 남기고 잘라갈수있는 최대 높이구하기
for i in range(1,N):
    h = tree[i]
    res = [t-h for t in tree]
    sumt = sum(res)
    if sumt>M:#자른게 N보다 커지는 순간
        #i번째와 i-1번째 사이의 tree값이 답이 될거니까 찾으러가야됨
        print(h-math.ceil((M-sumt)/i))#만약 4를 채워야되는데 i가 3이면 3개 나무 가지고 4를 채워야되므로 높이가 1.3의 올림인 2씩 빠져야한다.
    elif sumt==M:
        print(h)

