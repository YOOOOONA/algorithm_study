# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 13:35:48 2019

@author: 융
"""

def repeat(t):
    for i in range(t):
        n,k=map(int,input().split())
        maxnum=solution(n,k)
        print("#"+repr(i+1),repr(maxnum))
def solution(n,k):
    paper=[]
    paper=input().split(" ")
    if (paper.count('0')==0):
        maxnum=0
        for i in range(1,k+1):
            i=repr(i)
            ct=paper.count(i)
            if(maxnum<ct):
                maxnum=ct
            #print("여기가 출력")
    else:
        not_exits=[]
        for i in range(1,k+1):
            if repr(i) not in paper:
                not_exits.append(repr(i))
        if not not_exits:
            #maxnum=0
            paper_=paper[::-1]
            print(paper, paper_)
            maxnum=paper.index('1')+1
            for j in range(2,k):
            
                ct=paper.index(repr(j+1))-(n-1-paper_.index(repr(j-1)))
                if(maxnum<ct):
                    maxnum=ct
            ct=n-1-paper_.index(repr(k-1))
            #print("문자열:",paper[0])
            print('이거?',paper.index(repr(1)),paper.index(repr(2)),paper.index(repr(3)))
            if(maxnum<ct):
                maxnum=ct
            
            #print("여기기기")
        
            
    return maxnum
def answer():
    t=int(input())
    repeat(t)
answer()