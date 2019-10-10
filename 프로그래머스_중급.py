# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 16:32:12 2019

@author: 융
"""
#3진법?
'''
def solution(n):#자연수 n을 124나라에서 쓰는 숫자로 바꿔라.n-1%3==0,1,2->1,2,4
    answer = ''
    cnt = 1
    
    while(True):
        if n<=3:
            if n==3:
                answer += str(4)
            else:
                answer += str(n)
        else:
            res=n//3
            while(res>3):
                res=res//3
                cnt+=1
            for i in range(cnt):
                
        
            answer+=switch(res)
            
    return answer

print(solution(4))
















def solution(n):
    if n<=3:
            if n==3:
                answer += str(4)
            else:
                answer += str(n)
            return answer
    gr=0
    for i in range(1,100):
        gr+=3**i
        if(n<gr):
            num=i
            break
    for i in range(num):#num개의 자리수
        n-=(3**(num-1)+1)
        n=switch(three(num,n))
        
def switch(x):
    return {0:'4',
            1:'1',
            2:'2' 
            }.get(x, "No data")
        

def three(num,n):
    th=''
    while(True):
        x//(3**(num-1))==
    

def solution2(n):
    answer=''
    while(n>3):
        q=(n%3)
        answer=switch(q)+answer
        n/=3
    if n<=3:
        answer+=switch(n)
'''
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
return answer



'''
1->몫=0 나머지=1       01
2->몫=0 나머지=2       02
3->몫=1 나머지 0       04
4->몫=1 나머지 1       11
5->몫=1 나머지 2       12
6->몫=2 나머지 0       14
7->몫=2-1 나머지 1       21
8
9->몫=3-1 나머지 0
10->




