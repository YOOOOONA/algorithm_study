# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 23:19:09 2019

@author: 융
"""#15 5 4 2 1...16 8 4 2 1.....16 15 5 4 2 1    17 15    18 6 2 1     19 18   20 10 
#m=[]

x=int(input())
mem=[0]*(x+1)#이거보다 어펜드해서 하나씩 추가로 받는게 낫긴함
for i in range(2,x+1):
   mem[i]=mem[i-1]+1
   if i%2==0:
       mem[i]=min(mem[i],mem[i//2]+1)
   if i%3==0:####이거 elif로 써가지고 한참 고민했다ㅠ..논리는 큰값을 할당받기위해 작은값부터 쌓아올라가는느낌
       mem[i]=min(mem[i],mem[i//3]+1)
print(mem[x])

n = int(input())
