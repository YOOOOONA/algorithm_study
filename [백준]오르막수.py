import sys
sys.stdin = open(".\\input.txt")
input = sys.stdin.readline

N = int(input())
dp = [[1 for _ in range(10)] for _ in range(N+1)]
for i in range(1,N):
    for j in range(1,10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(sum(dp[N-1])%10007)

# dp[1][1] = dp[1][0] + dp[0][1]
# dp[1][2] = dp[1][1] + dp[0][2]...원래는 1은 1부터 9까지의 걸 다 해야되는데 그냥 내림차순이라 생각해도똑같으니까..