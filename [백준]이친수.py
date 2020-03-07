# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 03:53:26 2020

@author: 융
"""

#dp문제..이진수 중 특별한 수 이친수: 0으로 시작하지 않고 1이 두 번 연속으로 나오지 않음
#10=>0  1  10  11  100  101  110   111   1000   1001   1010  이 중 이친수는 7개........아님!!!!!자리수 N임!!!!!!!
'''#십진수->이진수 코드 짰는데, 내장함수가 있었음 bin(십진수)==이진수
cnt=0
N_n=''
while(True):
    N_n=str(N%2)+N_n
    N=N//2
    if N>0: cnt+=1
    else: break 
'''

N=int(input())
'''
il='11'
cnt=0
bin(N)
for i in range(1,N+1):
    a=str(bin(i))
    if il in a:
        print(a)
    if il not in a:
        print("이친수:",a)
        cnt+=1
print(cnt)
'''

li=[0,1,1,2]
if N<=3:
    print(li[N])
else:
    for i in range(4,N+1):
        li.append(sum(li[:-1])+1)
    print(li[N])