# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:10:02 2019

@author: 융
"""
'''
k=[]
tot=0
ch=True
for i in range(9):
    j=int(input())
    tot+=j
    k.append(j)
#k.sort()#바로 이걸 프린트하면 안됨
#print(k)
for i in range(9):
    t=tot
    for j in range(i+1,9):
        t=t-k[i]-k[j]
        #print("확인",tot,t,i,j)
        if (t==100):
            del(k[i],k[j-1])
            ch=False
            break
    if (ch==False):
        break
k.sort()
for i in range(7):
    print(k[i])


import sys
 
# 전체 합 구하기
my_sum = 0
data = []
for _ in range(9):
    temp = int(sys.stdin.readline())
    data.append(temp)
    my_sum += temp
data.sort()
for i in range(9):
    for j in range(i+1,9):
        temp = data[i] + data[j]
        if my_sum - temp == 100:
            del(data[i],data[j-1])
            for k in range(7):
                print(data[k])
            sys.exit()

'''
import sys
n = 9
k = [int(input()) for _ in range(n)]#엔터로 받기
k.sort()
sum_k=sum(k)
for i in range(n):
    for j in range(i+1, n):
        if sum_k - k[i]-k[j] == 100:
            for m in range(n):
                if m!=i and m!=j:
                    print(k[m])
            sys.exit(0)
