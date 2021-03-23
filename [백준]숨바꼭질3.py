import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
N,K = map(int,input().split())
# 1 3
# 1 2 3
# 1 5
# 1 2 4 5

# 10 19
# 10 9 18 19

# #2
# 10 15
# 10 11 12 13 14 15;5
# 10 9 8 7 14 15;4

# #2
# 10 14
# 10 11 12 13 14;4
# 10 9 8 7 14;3

# #3
# 10 13
# 10 11 12 13;3=(K-N)
# 10 9 8 7 6 12 13;5=((N - K//2) +(1) )
answer = 0
while N != K:
    if N > K:#K가 작으면 빼는 수밖에없음
        answer += N - K
        N = K
    elif N < K < 2 * N:#3 ,2도
        answer += min((K-N),(N-K//2 + K%2))
        N = K
    elif 2 * N <= K:
        N *= 2
    else:
        print('여길들어와?',N,K)
if N == K:
    print(answer)