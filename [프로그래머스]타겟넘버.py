from heapq import heappush,heappop
def resort(heapq):
    #이미정렬돼있는 heapq
    q = [heappop(heapq),]
    while(heapq):
        pr,v,cnt = heappop(heapq)##[0,1,1], [0,-1,1]// [0,2,cnt]  [0,-1-1]//[5,3,cnt+cnt2]  ans+=cnt+cnt2
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


#파이써닉한 다른이이 풀이1
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

#파이써닉한 다른이이 풀이2
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

#dfs
def dfs(nums, i, n, t):
    ret = 0
    if i==len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret

def solution(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer

#bfs 그냥 이렇게 하면 될것을..
def solution(numbers, target):
    answer = 0
    queue = [(0, 0)]
    length = len(numbers)

    while queue:
        n = queue.pop()
        if n[0] < length:
            queue.append((n[0] + 1, n[1] + numbers[n[0] - 1]))
            queue.append((n[0] + 1, n[1] - numbers[n[0] - 1]))
        elif n[1] == target:
            answer += 1

    return answer