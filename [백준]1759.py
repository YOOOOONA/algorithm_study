import copy
import sys#대체 왜 안되는것?
sys.stdin = open('.\\input.txt')
input = sys.stdin.readline
#L:비밀번호 길이
L, C = map(int,input().split())
ch = sorted(list(input().split(' ')))#C개 문자열 :사용가능성있는 문자 종류
def comb(lst,n):#li=모음 또는 자음으로만 이뤄진 리스트,permLen=모음또는 자음으로 이뤄야할 조합의 길이
    #문자열 조합 
    #자음조합 & 모음 조합 따로 구해서 합친 후 정렬
    ret = []
    if n == 1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)-n+1):
            for temp in comb(lst[i+1:],n-1):
                ret.append([lst[i]]+temp)
    return ret
cb = comb(ch,L)
# def solve(L,ch):
#     #중복x,오름차순정렬,최소한개모음+최소두개자음
#     #사전식 출력
#     #문자열 하나끼고 자음 3개
#     #문자열 두개끼고 자음2개 #모음개수를 늘려가면서 조합을만들고 자음개수가 최소 두개를 충족할때까지 모음자음 조합을 만든다
#     mo,ja = [],[]
#     ansLi = []
#     for w in ch:
#         if w in ['a','e','i','o','u']:
#             mo.append(w)
#         else:
#             ja.append(w)
#     moLimit = min(L-2,len(mo))#모음개수가 딸리면 어쩔수없이 자음으로 채워야지#자음이 최소 두개는 있어야하므로 2개뺀게 모음의 최대 개수, 최소 개수는 1인데 그건 알아서 충족되겠지 .그럼 문자열 최소길이는 3<=L
#     jaLimit = len(ja)
    
#     for i in range(1,moLimit+1):#한개부터 한계까지 개수로 모음조합을 만들어
#         if L-i > jaLimit: continue#자음길이 부족하면 조합 못만듦
#         for j in comb(mo,i):
#             for k in comb(ja,L-i):
#                 ansLi.append(j+k)
                
#     return ansLi#비밀번호일수있는 모든 문자열
# # print(solve(L,ch))
# ansLi = solve(L,ch)
# for i in range(len(ansLi)):
#     ansLi[i] = sorted(ansLi[i])
# ansLi = sorted(ansLi)
# for w in ansLi:
#     print(''.join(w))

for c in cb:
    cnt = 0
    for w in c:
        if w in ['a','e','i','o','u']:
            cnt += 1
    if cnt>=1 and (L-cnt)>=2:
        print(''.join(c))