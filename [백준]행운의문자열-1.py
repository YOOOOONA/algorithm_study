import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline

def solution(n,p):
    global ans
    global cnt
    if n == 0:
        ans += 1
        return
    
    for k in cnt.keys():
        if cnt[k]>0 and k!=p:
            cnt[k]-=1
            solution(n-1,k)
            cnt[k]+=1

S = list(input())
cnt = {}
ans = 0
for s in S:
    if s not in cnt:
        cnt[s]=1
    else:
        cnt[s]+=1
solution(len(S),'')
print(ans)