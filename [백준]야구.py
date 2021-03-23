import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline


def dfs(cnt):
    global answer
    if cnt == 9:#9명 모두 순서를 다 골랐으면 계산해야지
        start, score = 0, 0

        for inning in prof:
            out, b1, b2, b3, plus = 0, 0, 0, 0, 0#1이닝에 3아웃이면 공수교대

            while (out <= 2):
                p = lineup[start]#start번째에 오는 선수번호 p
                if inning[p] == 0:#p번선수의 득점 값
                    out += 1
                    plus = 0
                elif inning[p] == 1:
                    plus,b3,b2,b1 = b3,b2,b1,1 
                elif inning[p] == 2:
                    plus,b3,b2,b1 = b3 + b2,b1,1,0
                elif inning[p] == 3:
                    plus,b3,b2,b1 = b3 + b2 +b1,1,0,0
                elif inning[p] == 4:
                    plus,b3,b2,b1 = b1 + b2 + b3 + 1,0,0,0
                score += plus
                start = (start + 1) % 9#쓰리아웃아니면 계속 돌아
        answer = max(answer,score)

    else:
        for i in range(9):
            if lineup[i] != -1:#이미 i번째 순서는 뽑았을 때 스킵 
                continue
            lineup[i] = cnt#i번째 순서에 cnt번 타자 온다
            dfs(cnt + 1)
            lineup[i] = -1

N = int(input())
prof = [list(map(int,input().split())) for _ in range(N)]#N*9
lineup = [-1 for _ in range(9)]
lineup[3] = 0#3번째에 치는 사람은 0번이다.
answer = 0
dfs(1)#0번타자는 이미 골라졌으니 1번타자로 dfs 모든경우 돌기 시작.
print(answer)


# from itertools import permutations,combinations
# import time
# st = time.time()
# for i in set(permutations([1,1,2,3,0,0,0,0,0],9)):
#     print(i,end='')
# end = time.time()
# a=end-st
# st = time.time()
# for i in permutations(range(1,9),8):
#     print(i,end='')
# end = time.time()
# print('\n',a,end-st)

