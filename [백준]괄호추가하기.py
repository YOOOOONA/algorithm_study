import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
from itertools import combinations
# from collections import deque
N = int(input())
op = list(input())
def do3(left, mid, right):
    if mid == '*':
        return int(left)*int(right)
    elif mid == '+':
        return int(left)+int(right)
    elif mid == '-':
        return int(left)-int(right)
    
def do(op):
    answer = 0
    mid = '+'
    i = 0
    while True:
        if op[i] == '(':
            answer = do3(answer, mid, do3(op[i+1],op[i+2],op[i+3]))
            i += 5
        else:
            if i == 0:
                answer = do3(op[0],op[1],op[2])
                i += 3
            else:
                answer = do3(answer,mid,op[i])
                i += 1
        if i<len(op)-1:
            mid = op[i]
            i += 1
        else:
            break
    return answer
# print(do("1-9-(1-9)-(1-9)-(1-9)-(1-9)"))  

def solution(N,op):
    # 3+8*7-9*2

    answer = 0
    pv = [i for i in range(0,N-1,2)]
    for i in range(1,len(pv)//2+1):
        
        for comb in combinations(pv,i):
            newOP = []
            st = 0
            for j in range(0,len(comb)):
                if j>=1 and comb[j]-comb[j-1] < 3:
                    break
                if comb[j] == 0:
                    newOP.extend(['(',*op[:3],')'])
                    st = 3
                else:
                    newOP.extend(op[st:comb[j]])
                    newOP.extend(['(',*op[comb[j]:comb[j]+3],')'])    
                    st = comb[j]+3
            if st<len(op):
                newOP.extend(op[st:])
            answer = max(answer,do(newOP))
    return answer
print(solution(N,op))
    # 1-9-(1-9)-(1-9)-(1-9)-(1-9)
    # 1-9 
    # -8 -(-8)