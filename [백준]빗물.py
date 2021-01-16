import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

H,W = map(int,input().split())#세로,가,가로
blocks = list(map(int,input().split()))#00이상의 블록 높이들
#비가 오면 고이는 빗물의 총량 리턴
def rain(blocks):
    totalRain = 0
    j=0
    for j in range(1,W-1):#끝까지안갈거임
        now = blocks[j]
        side = min(max(blocks[0:j-1+1]),max(blocks[j+1:]))
        if side>now:
            totalRain += side-now
        else:continue
    return totalRain
print(rain(blocks))
