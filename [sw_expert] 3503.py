
T=int(input())
for i in range(T):
    N=int(input())
    h=list(map(int,input().split()))
    h=sorted(h)
    li=[]
    
    while(True):
        a=[]
        a.append(h.pop())#최댓갓과
        if h:
            b=h.pop()
            li.append(b)
        a.extend(li)
        li=a
        if (len(li)==N):
            break
    m=[]
    for j in range(len(li)):
        if i==len(li)-1:
            m.append(abs(li[i]-li[0]))
        else:
            m.append(abs(li[i+1]-li[i]))
    answer=max(m)
    print("#%d %d" %(i+1,answer))
     
#남의 코드
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    j = sorted(map(int, input().split()))
    ans = 0
    
    for i in range(n-2):
        ans = max(ans, j[i+2] - j[i])
    print('#{} {}'.format(test_case, ans))
'''
3
7
13 10 12 11 10 11 12
5
2 4 5 7 9
8
6 6 6 6 6 6 6 6
'''