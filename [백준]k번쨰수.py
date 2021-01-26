import sys
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
N=int(input())
k = int(input())

"""
############이거 메모리 에러 남. 이분탐색으로 풀어야됨
ans = []
for i in range(0,N*N,N):
    I=i//N
    ans.extend([(I+1)*(a+1) for a in range(N)])
print(sorted(ans)[k])
"""
#k번째 수는 k보다 작거나 같음. 이 전제를 가지고 이분탐색할거임
st, end = 1,k
while st<=end:
    mid = (st+end)//2
    target = 0
    for i in range(1,N+1):#mid이하인 숫자의 개수 세기=행으로 나눈 몫이 개수가 됨. 1,2,3: 2이하 수의 개수=2//1.하지만 최대는 N
        target += min(N,mid//i)
    if target<k:
        st = mid + 1
    elif target>=k:#만약에 mid가 6이 됐어.그러면 target이 항상 k이상이란말이야. 왜냐면 중복된 숫자가 많아. 그래서 이 조건일 때 ans에 넣고 end를 mid보다 줄여버리면 그 다음 target이 지금의 target보다 커질일은 없어.그럼그냥 끝나는거야
        ans = mid
        end = mid-1
print(ans)