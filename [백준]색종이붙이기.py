# 1이 적힌 칸은 모두 색종이로 덮여져야 한다.
# 나가서는 안되고, 겹쳐도 안 된다. 
#  1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수
# 1을 모두 덮는 것이 불가능한 경우에는 -1
import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
###########
from collections import deque
import copy
from itertools import permutations
def makePpr(i,j,size,paper):
    #사이즈받아서 paper위치 리턴
    loc = []
    for y in range(i,i+size):
        for x in range(j,j+size):
            if y<0 or y>=10 or x<0 or x>=10 or paper[y][x] != 1:
                return False
            else:
                loc.append([y,x])

    return loc
def solution(paperOne,paper):
    #10줄짜리 종이
    # 25장으로 어케 덮을거?
    sizecnt = [5 for _ in range(5)]
    answer = 0
    for i in range(len(paperOne)):
        sty,stx = paperOne[i]
        if paper[sty][stx] == 1:
            for size in range(5,0,-1):
                if sizecnt[size-1] <= 0:#색종이 이 사이즈 안남아있을 때
                    continue
                loc = makePpr(sty,stx,size,paper)
                if not loc:#영역 벗어나거나 이미 색종이 덮었을떄
                    continue
                else:
                    sizecnt[size-1] -= 1
                    answer += 1
                    for pos in loc:
                        paper[pos[0]][pos[1]] = size+1#색종이로 덮은거
                        
                    break
    for i in range(10):
        if paper[i].count(1) != 0:
            return -1#1이 한개라도 있으면 안됨
    return answer#최소색종이 수
for t in range(8):
    paper = []
    paperOne = deque([])
    # paper = [list(map(int,input().split())) for _ in range(10)]
    for i in range(10):
        paperR = list(map(int,input().split()))
        paper.append(paperR)#전체 종이 배열
        for j in range(10):
            if paperR[j] == 1:
                paperOne.append([i,j])
    # if t<4:continuex`
    answer = 26
    if len(paperOne)==0:
        answer = 0
    else:
        for perm in permutations(paperOne,len(paperOne)):
            PO = perm#copy.deepcopy(paperOne)#.copy()
            PP = copy.deepcopy(paper)#.copy()
            ans = solution(PO,PP)
            i+=1
            answer = min(answer,ans) if ans != -1 else answer
    answer = -1 if answer==26 else answer#answer갱신이 안됐으면 답없는거
    print('%dth answer:'%(t+1),answer)
    
111
111
111