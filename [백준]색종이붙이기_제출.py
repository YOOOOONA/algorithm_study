import sys

input = sys.stdin.readline

def solution(x, y, cnt):
    #dfs
    global ans
    if y >= 10:
        ans = min(ans, cnt)
        return

    if x >= 10:
        solution(0, y+1, cnt)
        return

    if a[x][y] == 1:
        for k in range(5):#작은사이즈부터 큰사이즈
            if paper[k] == 5:
                continue
            if x + k >= 10 or y + k >= 10:
                continue

            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    if a[i][j] == 0:
                        flag = 1
                        break
                if flag:
                    break

            if not flag:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 0

                paper[k] += 1
                solution(x + k + 1, y, cnt + 1)
                paper[k] -= 1

                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        a[i][j] = 1#다시 1로 채워주는 것이 포인트
    else:
        solution(x + 1, y, cnt)


a = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(5)]
ans = 26
solution(0, 0, 0)
print(ans) if ans != 26 else print(-1)