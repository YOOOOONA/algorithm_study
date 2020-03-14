# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:35:30 2020

@author: 융
"""
'''
'''
def check(i,j):
    r=[0,0,1,-1]
    c=[1,-1,0,0]
    for k in range(4):
        while(True):
            i += r[k]
            j += c[k]
            if 0<=i<N and 0<=j<N and mat[i][j]!=0:
                print(i,",",j,"의",k,"방향은 막힘")
                break
'''
T=int(input())
for t in range(T):
    wall=[]
    mat=[]
    
    N=int(input())
    for i in range(N):
        for j in range(N):
            
'''
def DFS(cores,connect,core_cnt,mat,node):
    global max_core
    global min_node
    if core_cnt==len(cores):
        if max_core<=connect:
            if connect==max_core:
                if node<min_node: min_node=node
            else:
                max_core=connect
                min_node=node
    if wall[core_cnt]==1:
        DFS(cores,connect+1,core_cnt+1,mat,node)
    else:
        
                
        
    
    
T=int(input())
for t in range(T):
    N=int(input())
    mat=[]
    wall=[[0*i for i in range(N)] for _ in range(N)]
    mcnt=0
    #mat 입력받으면서 테두리 코어 개수 세기
    for i in range(N):
        if i==0 or i==N-1:
            li=list(map(int,input().split()))
            mat.extend(li)
            wall[i]=li
            #mcnt+=sum(li)
        else:
            li=list(map(int,input().split()))
            mat.extend(li)
            wall[i][0]=mat[i][0]
            wall[i][N-1]=mat[i][N-1]
            #mcnt+=li[0]+li[N-1]
    max_core=0
    min_node=1000000
    DFS(cores,0,0,mat,0)
    print("#%d %d",t,min_node)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    