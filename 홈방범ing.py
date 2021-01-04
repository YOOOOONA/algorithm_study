<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:46:13 2020

@author: 융
"""
import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def solution(N,M,maxProfit):
    maxH = 0
    #k를 늘려가는데 비용이 손해면 k늘리고 
    #일단 k는 mat크기보다 작을 때까지만 늘리기
    k = 1
    while(k*k+(k-1)*(k-1) <= maxProfit):
        pay = k*k + (k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                #if i != 1 or j != 4:continue
                #print(i,j,k)
                tot = 0
                ll = []
                for di in range(-(k-1), +(k-1) + 1):
                    dj = (k-1) - abs(di)
                    new_i = i+di
                    
                    if 0<=new_i<N:  
                        #print('k',k,'i,j:',i,j,'di',di,"new",new_i,dj)
                        l = mat[new_i][max(0,j - dj): min(N,(j + dj) + 1)]
                        #print(l)
                        tot += sum(l)
                if M*tot - pay >= 0 :#이익이 나기만 하면 그때의 최대의 집 수 리턴
                    
                    maxH = max(maxH,tot)   
        k += 1
    return maxH
    
T = int(input())
for tc in range(T):
    li = list(map(int, input().split()))
    N,M=li[0],li[1]
    mat = [list(map(int, input().split())) for _ in range(N)]
    maxProfit = 0
    for i in mat:
        maxProfit += sum(i)
    maxProfit *= M
    #if tc != 1: continue
    ans = solution(N,M,maxProfit)#N=5이상 20이하 mat 가&세, M=1이상 10이하 한 집이 지불하는 돈
 
    print("#{} {}".format(tc+1,ans))
=======
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 15:46:13 2020

@author: 융
"""
import sys
sys.stdin = open('sample_input.txt','r')
input = sys.stdin.readline

def solution(N,M,maxProfit):
    maxH = 0
    #k를 늘려가는데 비용이 손해면 k늘리고 
    #일단 k는 mat크기보다 작을 때까지만 늘리기
    k = 1
    while(k*k+(k-1)*(k-1) <= maxProfit):
        pay = k*k + (k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                #if i != 1 or j != 4:continue
                #print(i,j,k)
                tot = 0
                ll = []
                for di in range(-(k-1), +(k-1) + 1):
                    dj = (k-1) - abs(di)
                    new_i = i+di
                    
                    if 0<=new_i<N:  
                        #print('k',k,'i,j:',i,j,'di',di,"new",new_i,dj)
                        l = mat[new_i][max(0,j - dj): min(N,(j + dj) + 1)]
                        #print(l)
                        tot += sum(l)
                if M*tot - pay >= 0 :#이익이 나기만 하면 그때의 최대의 집 수 리턴
                    
                    maxH = max(maxH,tot)   
        k += 1
    return maxH
    
T = int(input())
for tc in range(T):
    li = list(map(int, input().split()))
    N,M=li[0],li[1]
    mat = [list(map(int, input().split())) for _ in range(N)]
    maxProfit = 0
    for i in mat:
        maxProfit += sum(i)
    maxProfit *= M
    #if tc != 1: continue
    ans = solution(N,M,maxProfit)#N=5이상 20이하 mat 가&세, M=1이상 10이하 한 집이 지불하는 돈
 
    print("#{} {}".format(tc+1,ans))
>>>>>>> 8912e574d4896c30f8fbe673f8374d993e5ac05e
  