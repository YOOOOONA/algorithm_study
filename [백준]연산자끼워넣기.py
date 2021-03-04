import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
def do(seq):
    #연산결과 리턴
    res = seq[0]
    for i in range(1,len(seq),2):
        if seq[i] in ['+','-','*','//']:
            op = seq[i]
            right = seq[i+1]
            if op == '+':
                res += right
            elif op == '-':
                res -= right
            elif op == '*':
                res *= right
            elif op == '//':
                if res < 0:
                    res = -(-(res) // right)
                elif res == 0:
                    return False
                else:
                    res //= right
        else:
            raise ValueError('wrong seq')
    return res
from itertools import permutations
N = int(input())
Alist = list(map(int,input().split()))
op = list(map(int,input().split()))
operation = []
for i in range(4):
    if i==0:
        operation.extend(['+']*op[i])
    elif i==1:
        operation.extend(['-']*op[i])
    elif i==2:
        operation.extend(['*']*op[i])
    elif i==3:
        operation.extend(['//']*op[i])
minval = 1000000000
maxval = -1000000000
for comb in set(permutations(operation,N-1)):
    seq = [Alist[0],]
    for i in range(N-1):
        seq.extend([comb[i],Alist[i+1]])
    # print(seq)
    # print(do(seq))
    cur = do(seq)
    minval = min(minval,cur)
    maxval = max(maxval,cur)
print(maxval)
print(minval)
    