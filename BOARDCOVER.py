# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:21:22 2019

@author: 융
"""

'''
예제 입력
3 
3 7 
#.....# 
#.....# 
##...## 
3 7 
#.....# 
#.....# 
##..### 
8 10 
########## 
#........# 
#........# 
#........# 
#........# 
#........# 
#........# 
########## 
예제 출력
0
2
1514
'''
'''
coverType=(((0,0),(1,0),(0,1)),
           ((0,0),(0,1),(1,1)),
           ((0,0),(1,0),(1,1)),
           ((0,0),(1,0),(1,-1)))

def set(board,y,x,type,delta):
    
    ok=True
    for i in range(3):
        ny=y+coverType[type][i][0]
        nx=x+coverType[type][i][1]
        
                        
        board[ny][nx]=int(board[ny][nx])+delta
        print(board[ny][nx])

        
        if(ny<0 or ny>=board.size() or nx<0 or nx>=board[0].size()):
            ok=False
        elif(board[ny][nx]>1):
            ok=False
            

    return ok
def cover(board,h,w):
    y=-1
    x=-1
    
    for i in range(w):
        
        for j in range(h):
            if(int(board[i][j])==0):
                x=i
                y=j
                break
        if(y!=-1):
            break
    if(y==-1):
        return 1
    ret=0
    for type in range(4):
        if(set(board,y,x,type,1)):
            ret+=cover(board)
            
        set(board,y,x,type,-1)
    return ret
            
for i in range(int(input())):
    h,w=map(int,input().split())
    board=input()
    board=board.replace('#','1')# str=str.replace('바꿀문자열','바뀐 후 문자열')
    board=board.replace('.','0')
    print(cover(board,h,w))

'''
#문제1: 보드를 다차원행렬로 받기를 모르겠음 문제2: 엔터를 뭐로 받아야 사라지지
board=[][]
for i in range(3):
    b=input().strip(' ')
    b=b.replace('#','1')# str=str.replace('바꿀문자열','바뀐 후 문자열')
    b=b.replace('.','0')
    board[i]=list(b)
print(board)
print('a')





























