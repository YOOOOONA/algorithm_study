# -*- coding: utf-8 -*-
"""
Created on Wed May  8 11:33:56 2019

@author: 융
"""
"""
'''
3 
2 1 
0 1 
4 6 
0 1 1 2 2 3 3 0 0 2 1 3 
6 10 
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5'''

#n=int(input())#케이스 수
#m,p=input().split()#학생 수 , 친구 순서쌍 수
#m=int(m)
#p=int(p)
p=10
m=6######
friends=input().split()#순서쌍 나열
friends=list(map(int,friends))
#print(friends)
s=[]
i=0
while(i<2*p-1):
    s.append(list(set(friends[i:i+2])))#오호 sorted를 안하고 set만 했을 뿐인데 알아서 정렬이 되네!
    i=i+2
s=sorted(s)
print(s)
count=0
num=[]
cnt=[0 for _ in range(m-2)]

for j in range(p):
    
    if s[j][0]==0:
        count+=1
        num.append(s[j][1])
    elif(s[j][0]<=m-3):
        
        cnt[s[j][0]]+=1
    else:
        break
  
print('num:',num,'cnt:',cnt)
    

'''
젤 큰 숫자보다 3개 작은거 까지만 개수세면됨
01:
    23
02:
    13
03:
    12
    
01 :
    23 45 or 24 35
02 :
    13 45 or 14 25
'''
"""
n=0
areFriends=[]
def countPairings(taken):
    firstFree=-1
    for i in range(n):
        if(not taken[i]):
            firstFree=i
            break
    if(firstFree==-1):
        return 1
    
    ret=0    
    for pairWith in range(firstFree+1,n):
        if(not taken[pairWith] and areFriends[firstFree][pairWith]):
            taken[firstFree]=taken[pairWith]=True
            ret+=countPairings(taken)
            taken[firstFree]=taken[pairWith]=False
    return ret

C=int(input())
for k in range(C):
    areFriends=[[False]*10 for i in range(10)]
    n,m=map(int,input().split())
    friendsList=[int(x) for x in input().split()]
    
    for i in range(len(friendsList)//2):
        areFriends[friendsList[i*2]][friendsList[i*2+1]]=True
        areFriends[friendsList[i*2+1]][friendsList[i*2]]=True
    print(countPairings([False for j in range(n)]))
        












