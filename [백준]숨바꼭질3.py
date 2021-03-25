

#  st = time.time();if visited[18]:print(18);end=time.time();print(end-st)
#  st = time.time();if 3 in visited2:print(3);end=time.time();print(end-st)#뭐가 더 빠를까?

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
# answer = 0
# while N != K:
#     if N > K:#K가 작으면 빼는 수밖에없음
#         answer += N - K
#         N = K
#     elif N < K < 2 * N:#3 ,2도
#         answer += min((K-N),(N-K//2 + K%2))
#         N = K
#     elif 2 * N <= K:
#         N *= 2
#     else:
#         print('여길들어와?',N,K)
# if N == K:
#     print(answer)
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
N,K = map(int,input().split())
visited = [0 for _ in range(100001)]

from heapq import heappop,heappush
answer = 100000
def bfs(start):
    global answer
    q = [[0,start],]
    visited[start] = 1
    while q:
        time,cur = heappop(q)
        if answer < time:
            continue
        if cur == K:
            answer = min(answer,time)
        else:
            if cur+1 <100001 and visited[cur + 1] == 0:
                visited[cur + 1] = 1#얘를 다시 0으로 안만들고 걍 while돌아도되는이유: cur+1을 간다는건  나머지 두 방향으로 가도 다시 이 점으로 안온다는 거임
                heappush(q,[time+1,cur+1])
            if cur-1>=0 and visited[cur - 1] == 0  :
                visited[cur - 1] = 1
                heappush(q,[time+1,cur-1])
            if  cur*2 <100001 and visited[cur * 2] == 0 :
                visited[cur * 2] = 1
                heappush(q,[time,cur * 2])

bfs(N)
print(answer)