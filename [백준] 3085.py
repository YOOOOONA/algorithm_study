# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 11:57:08 2020

@author: 융
"""
'''
import copy
def ccnt(M,s): 
    global N
    cnt=0
    print("시작?")
    for i in range(N-1):  
        #print(s)
        if (s[i]==s[i+1]):
            cnt+=1
        else:
            cnt=0
        #마지막 인덱스까지 최장길이에 포함시켜주는거 놓치기 쉬움
        if i==N-2 and s[i]==s[i+1]:
            cnt+=1
        M=max(M,cnt)
    return M

#0행에서 제일 긴 열 찾기
M=0
def find_row(M,r_num,n_matrix):
    
    s=n_matrix[r_num]
    #print("type:",type(s[0]),"s:",s)
    M=ccnt(M,s)
    return M
#0열에서 제일 긴 행 찾기
def find_col(M,c_num,n_matrix):
    s=[n_matrix[i][c_num] for i in range(N)]
    #print("type:",type(s[0]),"s:",s)
    M=ccnt(M,s)              
    return M

def swap(a,b):
    tmp=a
    a=b
    b=tmp
    return a,b

if __name__=='__main__':
    N=int(input())
    M=0
    matrix=[]
    for i in range(N):
        #띄어쓰기 없을 때 글자 한개씩 리스트에 넣어서 이차 행렬 만들기
        matrix.append(list(input()))
    
    for i in range(N):
        for j in range(N-1):
            n_matrix=copy.deepcopy(matrix)
            print(i,"행의 ",j,"열과 ",j+1,"열")
            n_matrix[i][j],n_matrix[i][j+1]=swap(n_matrix[i][j],n_matrix[i][j+1])#같은 행 내에서 바꾸기
            #j열이랑 j+1열이랑 i행 내에서 최댓값 확인해야됨 여기서  max지정하기
            
            M=find_col(M,j,n_matrix)
            M=find_col(M,j+1,n_matrix)
            M=find_row(M,i,n_matrix)
            #for k in range(N):
            #    print(n_matrix[k],"\n")
            #print(M)
            n_matrix=copy.deepcopy(matrix)
            n_matrix[j][i],n_matrix[j+1][i]=swap(n_matrix[j][i],n_matrix[j+1][i])#같은 행 내에서 바꾸기
            #print(i,"열의 ",j,"행과 ",j+1,"행")
            #j열이랑 j+1열이랑 i행 내에서 최댓값 확인해야됨 여기서  max지정하기
            M=find_row(M,j,n_matrix)
            M=find_row(M,j+1,n_matrix)
            M=find_col(M,i,n_matrix)
            #for l in range(N):
            #    print(n_matrix[l],"\n")            
            #print(M)
'''
import copy
import sys
def ccnt(M,s): 
    global N
    cnt=0
    for i in range(N-1):  
        if (s[i]==s[i+1]):
            cnt+=1
        else:
            cnt=0
        if i==N-2 and s[i]==s[i+1]:
            cnt+=1
        M=max(M,cnt)
    return M

M=0
def find_row(M,r_num,n_matrix):
    
    s=n_matrix[r_num]
    M=ccnt(M,s)
    return M
def find_col(M,c_num,n_matrix):
    s=[n_matrix[i][c_num] for i in range(N)]
    M=ccnt(M,s)              
    return M

def swap(a,b):
    tmp=a
    a=b
    b=tmp
    return a,b
def ch(M):
    global N
    if M==N:
        print(M)
        sys.exit(0)
if __name__=='__main__':
    N=int(input())
    M=0
    matrix=[]
    for i in range(N):
        matrix.append(list(input()))
    
    for i in range(N):
        for j in range(N-1):
            n_matrix=copy.deepcopy(matrix)
            n_matrix[i][j],n_matrix[i][j+1]=swap(n_matrix[i][j],n_matrix[i][j+1])            
            M=find_col(M,j,n_matrix)
            ch(M)
            M=find_col(M,j+1,n_matrix)
            ch(M)
            M=find_row(M,i,n_matrix)
            ch(M)
            n_matrix=copy.deepcopy(matrix)
            n_matrix[j][i],n_matrix[j+1][i]=swap(n_matrix[j][i],n_matrix[j+1][i])
            M=find_row(M,j,n_matrix)
            ch(M)
            M=find_row(M,j+1,n_matrix)
            ch(M)
            M=find_col(M,i,n_matrix)
            ch(M)
    print(M)
'''시간초과'''
'''
import copy
a=[[1,2],[4,5]]          
b=[]
b=copy.deepcopy(a)
a[0][0] =5
print(b,a) 
if 'a'=='b':
    print("False")
else:
    print("True")
'''
"""
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
"""

