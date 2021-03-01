import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
import math
N = int(input())
Alist = list(map(int,input().split()))#강의실 별 응시자 수
B,C = map(int,input().split())#총감 가능 / 부감 가능
def solution():
    #총감은1명, 부감여러명가능
    answer = 0
    for a in Alist:
        if a-B<=0:
            answer += 1
        else:
            answer += 1 + math.ceil((a-B) / C)

    return answer#필요한 감독관 수의 최솟값
print(solution())