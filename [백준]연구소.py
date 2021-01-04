import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline
def f(n, s): 
    global minV
    # 13월은 없으니까
    ## 이상으로 하는 이유는 12월에 3개월권을 끊어야 할 경우=>wow이건 생각못했다.
    if(n >= 13):
        if(s < minV):
            minV = s
    # 1 ~ 12월
    else:
        # n월에 1일권 구입
        f(n+1, s+d*month[n])
        # n월에 1개월권 구입
        f(n+1, s+m)
        # n월에 3개월권 구입
        f(n+3, s+m3)#아,, 연속으로 헬스장을 갔는지 아닌지는 체크할 필요가없음.걍 모든 경우의 수 다 계산해서 젤 작은거 리턴하면 됨.

T = int(input())
for tc in range(T):
    d, m, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))
    # 1년 이용권과 비교
    minV = y
    # 1월부터, 1월 이전 이용금액 0 원
    f(1, 0)
    print("#{} {}".format(tc+1, minV))