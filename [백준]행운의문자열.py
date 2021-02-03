#인접해 있는 모든 문자가 같지 않은 문자열
#문자열 S에 나오는 문자를 재배치하면 서로 다른 행운의 문자열이 몇 개 나오는지 
#원래 문자열 S도 행운의 문자열이라면 그것도 개수에 포함
import sys
from itertools import permutations
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
#모든 조합을 다 구하고 생각하는게 메모리 에러가 났음
def check(perm):
    #행운의문자열인지 쳌
    for i in range(1,len(perm)):
        if perm[i-1] == perm[i]:
            return False
    return True
def solution(S):# S의 길이는 최대 10이고, 알파벳 소문자
    cnt = 0
    for p in set(permutations(S,len(S))):
        if check(p):
            cnt += 1 
    return cnt
S = list(input())
print(solution(S))
