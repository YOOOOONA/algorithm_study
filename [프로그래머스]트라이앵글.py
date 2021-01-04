# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:49:01 2020

@author: 융
"""
'''

def recur(sp,res,triangle,move,answer):
    #global answer
    if sp[0] > len(triangle) - 2:
        
        answer = max(answer,res)
        print(answer)
        return answer
    for i in range(2):
        nX, nY = sp[0] + move[i][0], sp[1] + move[i][1]
        addV = triangle[nX][nY]
        recur((nX,nY),res+addV,triangle,move,answer)
        
def solution(triangle):
    answer = 0
    move = [(1,0),(1,1)]
    answer=recur((0,0),answer,triangle,move,answer)
    return answer

'''
def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    return max(triangle[-1])
print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))