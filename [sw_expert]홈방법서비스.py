# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 01:45:52 2020

@author: 융
"""

import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def solution(N,M):
    maxH = 0
    #k를 늘려가는데 비용이 손해면 k늘리고 
    #일단 k는 mat크기보다 작을 때까지만 늘리기
    k = 1
    while(k <= N+1):
        pay = k*k + (k-1)*(k-1)
        #print(k,pay,'\n\n\n\n\n\n\n')
        #mat_padding = [[0 for _ in range(N + 2*(k-1))] for _ in range(N + 2*(k-1))]
        ########cnt = 0
        for i in range(N):
            for j in range(N):
                #print(i,j)
                #if i!=14 or j != 14:continue
                tot = 0
                #print('여기서시작',i,j)
                #ll = []
                ######cnt += 1
                for di in range(-(k-1), +(k-1) + 1):
                    dj = (k-1) - abs(di)
                    new_i = i+di# max(0,i+di) if di<0 else min(N-1,i+di)
                    if 0<=new_i<N:  
                        #print('k',k,'i,j:',i,j,'di',di,"new",new_i,dj)
                        l = mat[new_i][max(0,j - dj): min(N-1,(j + dj) + 1)]
                        #ll.append(l)
                        ##########print(l)
                        tot += sum(l)
                ######if cnt == 10:
                    ######print('cnt',cnt)
                    #########return
                    #print(tot)
                    
                    #[i,j] 기준으로 [i-(k-1)][j], [i-(k-2)][j-1:j+1], 
                    #1칸이면 [i][j]
                    #2칸이면 [i - (2-1)][j], [i][j-1:j+1], [i + (2-1)][j]
                    #3칸이면 [i - (3-1)][j], [i - (3-2)][j - 1:j + 1]  ,[i][j-2:j+2], [i + (3-2)][j - 1:j + 1], [i + (3-1)][j]
                
                #i,j,k기준으로 포함할 수 있는 집 다 포함했음 
                if M*tot - pay >= 0 :#이익이 나기만 하면 그때의 최대의 집 수 리턴
                    ###########print(tot)
                    maxH = max(maxH,tot)   
                    '''
                    print(N,"영역",k,'[',i,j,']')
                    for i in range(len(ll)):
                        print(i,' '*(N-len(ll[i])),ll[i])
                    print('답은',tot,'\n')
                    '''
                    #break
                
    
    
        k += 1
        #########33break
    return maxH
    
T = int(input())
for tc in range(T):
    
    #print((map(int,input().split())))
    #N,M= map(int,input().split())
    li = list(map(int, input().split()))
    N,M=li[0],li[1]
    #print(li)
    mat = [list(map(int, input().split())) for _ in range(N)]
    #if tc != 4 : continue
    #print(mat)
    ans = solution(N,M)#N=5이상 20이하 mat 가&세, M=1이상 10이하 한 집이 지불하는 돈
 
    print("#{} {}".format(tc+1,ans))
    #break
'''
a=[[2,3,4],[0,1,2]]
s=0
print((lambda x: sum(x), a))
s += (lambda x: sum(x), a)
'''