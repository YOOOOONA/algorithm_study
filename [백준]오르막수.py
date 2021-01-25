import sys
sys.stdin = open(".\\input.txt")
input = sys.stdin.readline

N = int(input())
dp = [[1 for _ in range(10)] for _ in range(N+1)]
for i in range(1,N):
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(sum(dp[N-1])%10007)