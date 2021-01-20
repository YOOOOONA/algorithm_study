from heapq import heappush,heappop
def resort(heapq):
    #이미정렬돼있는 heapq
    q = [heappop(heapq),]
    while(heapq):
        pr,v,cnt = heappop(heapq)
        if q[-1][0]==pr and q[-1][1]==v:####복붙하다가 1아니라 0으로 인덱스 줘서 틀렸었음
            q[-1][2]+=cnt
        else:
            q.append([pr,v,cnt])
    return q
def solution(numbers,target):
    ans = 0
    #걍 모든 경우의 수 다 bfs로 돌아
    #근데 순서대로 도는데 priority와 값이 같다? 그러면 cnt를 합쳐서 ans에 cnt더해주기:resort
    cnt = 1
    q = []
    heappush(q,[0,numbers[0],cnt])
    heappush(q,[0,(-1)*numbers[0],cnt])
    
    while q:
        q = resort(q)
        pr,v,cnt = q.pop(0)
        if pr<len(numbers)-1:
            q.append([pr+1,v+numbers[pr+1],cnt])###numbers[pr] 로 해서 틀렸었음
            q.append([pr+1,v-numbers[pr+1],cnt])
        elif pr==len(numbers)-1 and v==target:
            ans+=cnt
    return ans
print(solution(	[2,3,5,7,9], 2))